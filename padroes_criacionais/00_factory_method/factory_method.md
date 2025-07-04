# Padrão de Projeto: Factory Method

O **Factory Method** é um padrão **criacional** que fornece uma interface para criar objetos em
uma superclasse, mas permite que as subclasses alterem o tipo de objetos que serão criados.

Ele ajudar a **desacoplar** o código cliente da lógica de criação de objetos, favorecendo a
extensabilidade.

## Intenção

Evitar instanciar objetos diretamente com `new` (ou no caso do Python, com chamadas diretas ao
construtor) e, em vez disso, delegar a criação para subclasses ou métodos especializados.

## Estrutura

### Participantes principais:

- **Creator (Criador)**: define o método de fábrica (`factory_method`) que retorna objetos
do tipo `Product`.
- **ConcreteCreator (Criador Concreto)**: sobreescreve o método de fábrica e retorna uma
instância específica de `Product`.
- **Product (Produto)**: define a interface comum dos objetos criados.
- **ConcreteProduct (Produto Concreto)**: implementa a interface do `Product`.

## Exemplo em Python

Vamos criar um exemplo com transporte:

```py
from abc import ABC, abstractmethod

# Interface do Produto
class Transporte(ABC):
    @abstractmethod
    def entregar(self) -> str:
        pass

# Produtos Concretos
class Caminhao(Transporte):
    def entregar(self) -> str:
        return "Entrega feita por caminhão."

class Navio(Transporte):
    def entregar(self) -> str:
        return "Entrega feita por navio."

# Criador
class Logistica(ABC):
    @abstractmethod
    def criar_transporte(self) -> Transporte:
        pass

    def planejar_entrega(self) -> str:
        transporte = self.criar_transporte()
        return transporte.entregar()

# Criadores Concretos
class LogisticaRodoviaria(Logistica):
    def criar_transporte(self) -> Transporte:
        return Caminhao()

class LogisticaMaritima(Logistica):
    def criar_transporte(self) -> Transporte:
        return Navio()

# Cliente
def client_code(logistica: Logistica) -> None:
    print(logistica.planejar_entrega())

# Teste
if __name__ == "__main__":
    print("Usando logística rodoviária:")
    client_code(LogisticaRodoviaria())

    print("\nUsando logística marítima:")
    client_code(LogisticaMaritima())
```

## Vantagens

- Evita acoplamento com classes concretas
- Facilita a extensão do código sem modificar o cliente
- Aplica o Princípio Aberto/Fechado (Open/Closed)

## Desvantagens

- Pode adicionar complexidade desnecessária quando poucas subclasses são usadas
- Mais classes para manter e entender

## Quando usar?

- Quando você não sabe da antemão o tipo de objeto que precisará instanciar
- Quando quer permitir a extensão do sistema sem alterar código existente
- Quando diferentes implementações precisam ser intercambiáveis

## Referência
[Refactoring Guru – Factory Method](https://refactoring.guru/pt-br/design-patterns/factory-method)