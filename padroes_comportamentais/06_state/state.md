# Padrão de Projeto: State

O padrão **State** permite que um objeto **altere seu comportamento** quando seu estado interno
muda, como se o objeto **mudasse de classe** em tempo de execução.

Ideal para **máquinas de estado**, onde cada estado encapsula lógica específica e sabe
quando e como transitar para o próximo.

## Intenção

Permitir que um objeto **mude seu comportamento** quando seu estado interno muda, evitando 
condicionais gigantescas (`if/else`, `switch/case`) espalhadas pelo código.

## Estrutura

### Participantes:

- **Context**: objeto que possui um estado e delega as ações para ele.
- **State (interface)**: interface comum para todos os estados.
- **ConcreteState**: implementações específicas do estado que executam comportamentos e definem
transições

## Exemplo em Python

Vamos simular uma **máquina de música** com três estados: Parada, Tocando, e Pausada.

```py
from abc import ABC, abstractmethod

# Interface de Estado
class Estado(ABC):
    @abstractmethod
    def play(self, player): pass

    @abstractmethod
    def pause(self, player): pass

    @abstractmethod
    def stop(self, player): pass

# Estados concretos
class Tocando(Estado):
    def play(self, player):
        print("▶️ Já está tocando.")

    def pause(self, player):
        print("⏸️ Pausando música.")
        player.estado = Pausado()

    def stop(self, player):
        print("⏹️ Parando reprodução.")
        player.estado = Parado()

class Pausado(Estado):
    def play(self, player):
        print("▶️ Retomando música.")
        player.estado = Tocando()

    def pause(self, player):
        print("⏸️ Já está pausado.")

    def stop(self, player):
        print("⏹️ Parando música.")
        player.estado = Parado()

class Parado(Estado):
    def play(self, player):
        print("▶️ Iniciando música.")
        player.estado = Tocando()

    def pause(self, player):
        print("⛔ Não é possível pausar. Música está parada.")

    def stop(self, player):
        print("⏹️ Já está parado.")

# Contexto
class PlayerMusica:
    def __init__(self):
        self.estado = Parado()

    def play(self):
        self.estado.play(self)

    def pause(self):
        self.estado.pause(self)

    def stop(self):
        self.estado.stop(self)

# Cliente
if __name__ == "__main__":
    player = PlayerMusica()

    player.play()
    player.pause()
    player.play()
    player.stop()
    player.pause()
```

## Vantagens

- Remove condicionais complexas baseadas em estado
- Adere ao princípio **aberto/fechado**: novos estados sem alterar código existente
- Cada estado tem sua **lógica isolada**

## Desvantagens

- Pode gerar **muitas classes** se houver muitos estados
- Transições de estado implícitas podem ser difíceis de rastrear

## Quando usar?

- Quando um objeto tem comportamento diferentes conforme o estado
- Quando há **máquinas de estado, workflows** ou **ciclos de vida complexos**
- Quando quer eliminar `if` ou `switch` repetitivos

## Comparações

Padrão   | Diferença principal
-------- | -----------------------------------------
State    | Muda comportamento de acordo com estado
Strategy | Muda algoritmo de acordo com configuração
Observer | Reage a eventos externos

## Referência
[Refactoring Guru – State](https://refactoring.guru/pt-br/design-patterns/state)