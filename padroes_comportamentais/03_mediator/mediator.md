# Padrão de Projeto: Mediator

O padrão **Mediator** define um **objeto central** (mediador) que encapsula a forma como
um conjunto de objetos interage. Em vez de os objetos se referirem uns aos outros
diretamente, eles usam o mediador.

Ideal para sistemas onde **muitos objetos se comunicam entre si**, e você quer **centralizar**
a lógica de interação.

## Intenção

Evitar comunicação direta entre objetos, promovendo um baixo acoplamento e
**facilitando a manutenção e expansão** do sistema.

## Estrutura

### Participantes:

- **Mediator**: interface comum do mediador.
- **ConcreteMediator**: implementação concreta que coordena a comunicação
- **Colleague**: componentes que se comunicam apenas com o mediador
- **ConcreteColleague**: implementação dos colegas que delegam interações ao mediador

## Exemplo em Python

Vamos simular um **sistema de chat** onde usuários se comunicam por meio de um 
**mediador (Sala de Bate-Papo)**.

```py
from abc import ABC, abstractmethod

# Mediator
class SalaDeChat(ABC):
    @abstractmethod
    def enviar(self, mensagem: str, remetente):
        pass

# Colleague
class Usuario:
    def __init__(self, nome: str, sala: SalaDeChat):
        self.nome = nome
        self.sala = sala

    def enviar(self, mensagem: str):
        print(f"📤 {self.nome} diz: {mensagem}")
        self.sala.enviar(mensagem, self)

    def receber(self, mensagem: str, remetente):
        print(f"📩 {self.nome} recebeu de {remetente.nome}: {mensagem}")

# ConcreteMediator
class SalaConcreta(SalaDeChat):
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, usuario: Usuario):
        self.usuarios.append(usuario)

    def enviar(self, mensagem: str, remetente):
        for usuario in self.usuarios:
            if usuario != remetente:
                usuario.receber(mensagem, remetente)

# Cliente
if __name__ == "__main__":
    sala = SalaConcreta()

    alice = Usuario("Alice", sala)
    bob = Usuario("Bob", sala)
    carla = Usuario("Carla", sala)

    sala.adicionar_usuario(alice)
    sala.adicionar_usuario(bob)
    sala.adicionar_usuario(carla)

    alice.enviar("Oi, pessoal!")
    bob.enviar("E aí, tudo bem?")
```

## Vantagens 

- Reduz a **acoplamento direto** entre objetos
- Centraliza a lógica de comunicação
- Facilita manutenção, testes e escabilidade
- Permite adicionar novos componentes sem alterar os existentes

## Desvantagens

- Pode se tornar um **Deus Objeto** se crescer demais
- Exige cuidado para manter a Mediator coeso e modular

## Quando usar?

- Quando objetos se comunicam de forma complexa ou redundante
- Quando você quer **centralizar a lógica de interação**
- Quando precisa de **baico acoplamento** entre classes

## Exemplos reais

- Sistemas de GUI (botões, inputs, menus)
- Frameworks de front-end (React, Angular, etc.)
- Central de eventos, chats, mensagerias

## Referência
[Refactoring Guru – Mediator](https://youtu.be/eNcvblM8-_o?list=RDAupwoN8QvbU)