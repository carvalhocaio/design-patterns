# Padrão de Projeto: Flyweight

O padrão **Flyweight** tem como objetivo **compartilhar objetos** para suportar eficientemente
grandes quantidades de instâncias com dados semelhantes, economizando **memória**.

Ideal para sistemas com **milhares de objetos repetidos**, como renderização de gŕaficos, textos,
jogos, etc.

## Intenção

Reduzir o uso de memória **compartilhando o estado interno** de objetos semelhantes e mantendo o 
estado externo fora.

## Estrutura

### Conceitos-chave:

- **Estado intrínseco**: compartilhado e imutável (ex: cor, tipo).
- **Estado extrínseco**: passado pelo cliente e **não compartilhado** (ex: posição, contexto).

### Participantes

- **Flyweight (Peso Leve)**: interface comum.
- **ConcreteFlyweight**: implementação do objeto compartilhado.
- **FlyweightFactory**: garante reutilização de objetos existentes.
- **Client**: fornece dados externos e usa os Flyweights.

## Exemplo em Python

Vamos modelar um sistema de **exibição de árvores em um mapa**, onde milhares de árvores
são criadas, mas cores e tipos podem ser compartilhados.

```py
# Flyweight
class TipoArvore:
    def __init__(self, nome, cor, textura):
        self.nome = nome
        self.cor = cor
        self.textura = textura

    def renderizar(self, x, y):
        print(f"🌳 {self.nome} ({self.cor}, {self.textura}) em posição ({x},{y})")

# Flyweight Factory
class FabricaTiposArvore:
    _tipos = {}

    @classmethod
    def obter_tipo(cls, nome, cor, textura):
        chave = (nome, cor, textura)
        if chave not in cls._tipos:
            cls._tipos[chave] = TipoArvore(nome, cor, textura)
        return cls._tipos[chave]

# Contexto (estado extrínseco)
class Arvore:
    def __init__(self, x, y, tipo: TipoArvore):
        self.x = x
        self.y = y
        self.tipo = tipo

    def renderizar(self):
        self.tipo.renderizar(self.x, self.y)

# Cliente
class Floresta:
    def __init__(self):
        self.arvores = []

    def plantar_arvore(self, x, y, nome, cor, textura):
        tipo = FabricaTiposArvore.obter_tipo(nome, cor, textura)
        self.arvores.append(Arvore(x, y, tipo))

    def renderizar(self):
        for arvore in self.arvores:
            arvore.renderizar()

# Teste
if __name__ == "__main__":
    floresta = Floresta()
    floresta.plantar_arvore(1, 2, "Ipê", "Amarelo", "Lisa")
    floresta.plantar_arvore(3, 4, "Ipê", "Amarelo", "Lisa")
    floresta.plantar_arvore(5, 6, "Jacarandá", "Roxo", "Cascuda")

    floresta.renderizar()

    print("\nTotal de tipos únicos:", len(FabricaTiposArvore._tipos))
```

## Vantagens

- Reduz uso de memória
- Melhora desempenho em aplicações com muitos objetos repetidos
- Segue os principíos de reutilização e economia de recursos

## Desvantagens

- Complexidade extra na separação de estados intrínsecos/extrínsecos
- Nem sempre útil se os objetos forem muito diferentes

## Quando usar?

- Quando há **muitos objetos semelhantes** (ex: jogos, UIs, editores de texto)
- Quando precisa **economizar memória**
- Quando os dados compartilháveis são **imutáveis**

## Referência
[Refactoring Guru – Flyweight](https://refactoring.guru/pt-br/design-patterns/flyweight)