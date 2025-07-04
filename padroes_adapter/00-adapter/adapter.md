# Padrão de Projeto: Adapter

O padrão **Adapter** permite que interfaces incompatíveis **trabalhem juntas**. Ele atua como
um **tradutor** entre duas interfaces, adaptando uma interface existente para que o código
cliente possa usá-la como se fosse compatível.

Ideal quando você precisa **reutilizar** uma classe que tem uma interface diferente da esperada.

## Intenção

Converter a interface de uma classe em outra interface que o cliente espera. Assim, classes
com interfaces incompatíveis podem trabalhar juntas sem alterar seu código.

## Estrutura

### Participantes

- **Target (Alvo)**: interface que o cliente espera.
- **Client (Cliente)**: usa objetos conforme o contrato de `Target`.
- **Adaptee (Adaptado)**: classe existente com interface diferente.
- **Adapter (Adaptador)**: converte a interface de `Adaptee` para a de `Target`.

## Exemplo em Python

Vamos criar um cenário onde o cliente espera **um carregador com plugue europeu**, mas temos
**um carregador americano** que precisa de um adaptador.

```py
# Alvo (interface esperada pelo cliente)
class PlugUE:
    def conectar(self) -> str:
        return "Conectado com plugue europeu."

# Classe existente (incompatível)
class PlugUSA:
    def connect(self) -> str:
        return "Connected with US plug."

# Adaptador
class AdaptadorUSAtoUE(PlugUE):
    def __init__(self, plug_usa: PlugUSA):
        self.plug_usa = plug_usa

    def conectar(self) -> str:
        return self.plug_usa.connect()

# Cliente
def usar_carregador(plug: PlugUE):
    print(plug.conectar())

# Teste
if __name__ == "__main__":
    plug_europeu = PlugUE()
    usar_carregador(plug_europeu)

    print("---")

    plug_americano = PlugUSA()
    adaptador = AdaptadorUSAtoUE(plug_americano)
    usar_carregador(adaptador)
```

## Vantagens

- Permite a reutilização de código legado ou de terceiros sem modificações
- Desacopla o cliente da implementação original
- Segue o princípio aberto/fechado (Open/Closed)

## Desvantagens
 
- Pode aumentar a complexidade se mal utilizado
- Se houver muitos adaptadores, o código pode ficar difícil de manter

## Quando usar?

- Quando você usar uma classe existente, mas sua interface não é compatível
- Quando quer integrar bibliotecas de terceiros ou sistema legados
- Quando você não pode (ou não quer) alterar o código original

## Tipos de Adapter

- **Objeto (composição)**: o adaptador recebe uma instância da classe adaptada (exemplo acima).
- **Classe (herança)**: o adaptador herda diretamente da classe adaptada (não recomendado em  
Python por conta da flexibiidade com composição).

## Referência
[Refactoring Guru – Adapter](https://refactoring.guru/pt-br/design-patterns/adapter)