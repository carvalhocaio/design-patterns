from abc import ABC, abstractmethod

# Receiver (quem executa as ações reais)
class Luz:
    def ligar(self):
        print("💡 Luz ligada")

    def desligar(self):
        print("💡 Luz desligada")

# Command
class Comando(ABC):
    @abstractmethod
    def executar(self): pass

# Concrete Commands
class LigarLuz(Comando):
    def __init__(self, luz: Luz):
        self.luz = luz

    def executar(self):
        self.luz.ligar()

class DesligarLuz(Comando):
    def __init__(self, luz: Luz):
        self.luz = luz

    def executar(self):
        self.luz.desligar()

# Invoker
class ControleRemoto:
    def __init__(self):
        self._historico = []

    def executar_comando(self, comando: Comando):
        self._historico.append(comando)
        comando.executar()

# Cliente
if __name__ == "__main__":
    luz_sala = Luz()

    comando_ligar = LigarLuz(luz_sala)
    comando_desligar = DesligarLuz(luz_sala)

    controle = ControleRemoto()
    controle.executar_comando(comando_ligar)
    controle.executar_comando(comando_desligar)
