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
