from abc import ABC, abstractmethod

# Classe abstrata com o Template Method
class BebidaQuente(ABC):
    def preparar(self):
        self.esquentar_agua()
        self.adicionar_principal()
        self.adicionar_acompanhamentos()
        self.servir()

    def esquentar_agua(self):
        print("🔥 Esquentando água...")

    @abstractmethod
    def adicionar_principal(self):
        pass

    @abstractmethod
    def adicionar_acompanhamentos(self):
        pass

    def servir(self):
        print("🥤 Servindo bebida...\n")

# Subclasses concretas
class Cha(BebidaQuente):
    def adicionar_principal(self):
        print("🍃 Adicionando folhas de chá...")

    def adicionar_acompanhamentos(self):
        print("🍋 Adicionando limão...")

class Cafe(BebidaQuente):
    def adicionar_principal(self):
        print("☕ Adicionando pó de café...")

    def adicionar_acompanhamentos(self):
        print("🥄 Adicionando açúcar...")

# Cliente
if __name__ == "__main__":
    print("Preparando chá:")
    bebida = Cha()
    bebida.preparar()

    print("Preparando café:")
    bebida = Cafe()
    bebida.preparar()
