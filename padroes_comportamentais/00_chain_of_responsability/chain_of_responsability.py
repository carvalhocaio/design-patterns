from abc import ABC, abstractmethod

# Handler base
class Suporte(ABC):
    def __init__(self):
        self._proximo = None

    def definir_proximo(self, proximo):
        self._proximo = proximo
        return proximo

    @abstractmethod
    def tratar(self, problema: str):
        pass

# Manipuladores concretos
class Atendente(Suporte):
    def tratar(self, problema: str):
        if problema == "senha":
            print("🔧 Atendente: Resolvi o problema de senha.")
        elif self._proximo:
            print("↪️ Atendente: Encaminhando para o Supervisor...")
            self._proximo.tratar(problema)
        else:
            print("❌ Atendente: Não consigo resolver.")

class Supervisor(Suporte):
    def tratar(self, problema: str):
        if problema == "rede":
            print("🛠️ Supervisor: Resolvi o problema de rede.")
        elif self._proximo:
            print("↪️ Supervisor: Encaminhando para o Gerente...")
            self._proximo.tratar(problema)
        else:
            print("❌ Supervisor: Não consigo resolver.")

class Gerente(Suporte):
    def tratar(self, problema: str):
        if problema == "servidor":
            print("🚨 Gerente: Resolvi o problema no servidor.")
        else:
            print("❌ Gerente: Problema não identificado.")

# Cliente
if __name__ == "__main__":
    atendente = Atendente()
    supervisor = Supervisor()
    gerente = Gerente()

    atendente.definir_proximo(supervisor).definir_proximo(gerente)

    print("\nChamado: problema com senha")
    atendente.tratar("senha")

    print("\nChamado: problema de rede")
    atendente.tratar("rede")

    print("\nChamado: problema no servidor")
    atendente.tratar("servidor")

    print("\nChamado: problema desconhecido")
    atendente.tratar("hack")
