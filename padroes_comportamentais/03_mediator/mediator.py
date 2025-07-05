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
