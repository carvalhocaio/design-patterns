# Padrão de Projeto: Builder

O padrão **Builder** permite a construção de objetos complexos **etapa por etapa**, desacoplando
o processo de construção da representação final do objeto.

Ideal para criar objetos com muitas **configurações opcionais, combinações** ou **etapas de construção** que variam.

## Intenção

Separar a construção de um objeto complexo da sua representação final, de modo que o mesmo processo de construção possa criar diferentes representações.

## Estrutura

### Participates principais:

- **Builder (Construtor)**: interface comum para criar as partes do objeto.
- **ConcreteBuilder (Construtor Concreto)**: implementação da construção.
- **Product (Produto)** objeto final que está sendo construído.
- **Director (Diretor)** opcional; controla a ordem da construção.
- **Client (Cliente)**: coordena tudo e usa o builder.

## Exemplo em Python

Vamos modelar a construção de um **lanche** (hambúrguer, porção, bebida).

```py
from abc import ABC, abstractmethod

# Produto final
class Lanche:
    def __init__(self):
        self.itens = []

    def adicionar(self, item: str):
        self.itens.append(item)

    def mostrar(self):
        print("Lanche inclui:")
        for item in self.itens:
            print(f" - {item}")

# Builder (interface)
class LancheBuilder(ABC):
    @abstractmethod
    def adicionar_pao(self): pass

    @abstractmethod
    def adicionar_carne(self): pass

    @abstractmethod
    def adicionar_bebida(self): pass

    @abstractmethod
    def obter_lanche(self) -> Lanche: pass

# ConcreteBuilder
class LancheCheddarBuilder(LancheBuilder):
    def __init__(self):
        self.lanche = Lanche()

    def adicionar_pao(self):
        self.lanche.adicionar("Pão de brioche")

    def adicionar_carne(self):
        self.lanche.adicionar("Hambúrguer de carne com cheddar")

    def adicionar_bebida(self):
        self.lanche.adicionar("Refrigerante")

    def obter_lanche(self) -> Lanche:
        return self.lanche

# Outro Builder
class LancheVeganoBuilder(LancheBuilder):
    def __init__(self):
        self.lanche = Lanche()

    def adicionar_pao(self):
        self.lanche.adicionar("Pão integral")

    def adicionar_carne(self):
        self.lanche.adicionar("Hambúrguer de grão-de-bico")

    def adicionar_bebida(self):
        self.lanche.adicionar("Suco natural")

    def obter_lanche(self) -> Lanche:
        return self.lanche

# Diretor (opcional)
class Diretor:
    def __init__(self, builder: LancheBuilder):
        self._builder = builder

    def construir_lanche_completo(self):
        self._builder.adicionar_pao()
        self._builder.adicionar_carne()
        self._builder.adicionar_bebida()

# Cliente
if __name__ == "__main__":
    builder = LancheVeganoBuilder()
    diretor = Diretor(builder)
    diretor.construir_lanche_completo()

    lanche = builder.obter_lanche()
    lanche.mostrar()

    print("\n---\n")

    builder2 = LancheCheddarBuilder()
    diretor = Diretor(builder2)
    diretor.construir_lanche_completo()

    lanche2 = builder2.obter_lanche()
    lanche2.mostrar()
```

## Vantagens

- Criação **controlada passo a passo**
- Permite variações de objetos usando o mesmo processo
- Ótimo para objetos com **muitas combinações**

## Desvantagens

- Pode ser mais verboso
- Overkill para objetos simples

## Quando usar?

- Quando o objeto precisa de muitas configurações
- Quando a construção de um objeto é complexa ou dependente de várias etapas
- Quando você quer **reutilizar o processo** de construção para diferentes representações

## Referência
[Refactoring Guru - Builder](https://refactoring.guru/pt-br/design-patterns/builder)