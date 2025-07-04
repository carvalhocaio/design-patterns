# Padrão de Projeto: Abstract Factory

O **Abstract Factory** é um padrão **criacional** que fornece uma interface para criar
**famílias de objetos relacionados ou dependentes** sem especificar suas classes concretas.

Em vez de criar um objeto específico, você cria uma **fábrica inteira** que pode criar vários
objetos relacionais.

## Intenção

Permitir que o código cliente crie produtos que pertencem a uma mesma família (ex: interface
gráfica com botões e janelas) sem acoplamento direto às classes concretas desses produtos.

## Estrutura

### Participantes principais:

- **AbstractFactory (Fábrica Abstrata)**: declara métodos para criar produtos de diferentes tipos.
- **ConcreteFactory (Fábricas Concretas)**: implementam os métodos para criar variantes específicas.
- **AbstractProductA / AbstractProductB (Produtos Abstratos)**: interfaces comuns dos produtos.
- **ConcreteProdutctA1 / B1, A2 / B2**: implementações concretas dos produtos.
- **Client (Cliente)**: usa somente interfaces da fábricas e dos prodtuos.

## Exemplo em Python

Vamos modelar um sistema de interface gráfica que pode ter uma tema **Windows** ou **MacOS**.

```py
from abc import ABC, abstractmethod

# Produtos Abstratos
class Botao(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class Janela(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

# Produtos Concretos – Windows
class BotaoWindows(Botao):
    def render(self) -> str:
        return "Renderizando botão estilo Windows."

class JanelaWindows(Janela):
    def render(self) -> str:
        return "Renderizando janela estilo Windows."

# Produtos Concretos – Mac
class BotaoMac(Botao):
    def render(self) -> str:
        return "Renderizando botão estilo MacOS."

class JanelaMac(Janela):
    def render(self) -> str:
        return "Renderizando janela estilo MacOS."

# Fábrica Abstrata
class GUIFactory(ABC):
    @abstractmethod
    def criar_botao(self) -> Botao:
        pass

    @abstractmethod
    def criar_janela(self) -> Janela:
        pass

# Fábricas Concretas
class WindowsFactory(GUIFactory):
    def criar_botao(self) -> Botao:
        return BotaoWindows()

    def criar_janela(self) -> Janela:
        return JanelaWindows()

class MacFactory(GUIFactory):
    def criar_botao(self) -> Botao:
        return BotaoMac()

    def criar_janela(self) -> Janela:
        return JanelaMac()

# Cliente
class Aplicacao:
    def __init__(self, factory: GUIFactory):
        self.botao = factory.criar_botao()
        self.janela = factory.criar_janela()

    def renderizar_interface(self):
        print(self.botao.render())
        print(self.janela.render())

# Teste
def configurar_aplicacao(sistema: str) -> Aplicacao:
    if sistema == "Windows":
        return Aplicacao(WindowsFactory())
    elif sistema == "Mac":
        return Aplicacao(MacFactory())
    else:
        raise ValueError("Sistema não suportado.")

if __name__ == "__main__":
    app = configurar_aplicacao("Mac")
    app.renderizar_interface()
```

## Vantagens

- Garante que produtos de uma mesma **família** sejam compatíveis
- Ajuda a **isolar o código cliente** de classes concretas
- Segue o princípio da **inversão de dependência**

## Desvantagens

- A complexidade aumenta com o número de produtos e variantes
- Difícil adicionar novos tipos de produtos à família sem alterar interface

## Quando usar?

- Quando os objetos do sistema precisam ser criados em **grupos relacionados**
- Quando deseja garantir **consistência** entre os objetos que pertencem a uma família
- Qunado quer isolar o código cliente das classes concretas

## Referência
[Refactoring Guru – Abstract Factory](https://refactoring.guru/pt-br/design-patterns/abstract-factory)
