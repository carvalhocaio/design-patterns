# Subsistema
class Luz:
    def ligar(self):
        print("💡 Luzes acesas")

    def desligar(self):
        print("💡 Luzes apagadas")

class TV:
    def ligar(self):
        print("📺 TV ligada")

    def desligar(self):
        print("📺 TV desligada")

class Som:
    def ligar(self):
        print("🔊 Som ligado")

    def desligar(self):
        print("🔇 Som desligado")

# Facade
class HomeTheaterFacade:
    def __init__(self, luz: Luz, tv: TV, som: Som):
        self.luz = luz
        self.tv = tv
        self.som = som

    def assistir_filme(self):
        print("🎬 Preparando sessão de cinema...")
        self.luz.desligar()
        self.som.ligar()
        self.tv.ligar()

    def encerrar_filme(self):
        print("🛑 Encerrando sessão de cinema...")
        self.tv.desligar()
        self.som.desligar()
        self.luz.ligar()

# Cliente
if __name__ == "__main__":
    luz = Luz()
    tv = TV()
    som = Som()

    home_theater = HomeTheaterFacade(luz, tv, som)

    home_theater.assistir_filme()
    print("\n---\n")
    home_theater.encerrar_filme()
