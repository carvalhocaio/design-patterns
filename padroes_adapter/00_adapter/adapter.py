# Alvo (interface esperada pelo cliente)
class PlugUE:
    def conectar(self) -> str:
        return "Conectado com plugue europeu."

# Classe existente (incompatível)
class PlugUSA:
    def connect(self) -> str:
        return "Connected with US plug."

# Adaptador
class AdaptadorUSAtoUE(PlugUE):
    def __init__(self, plug_usa: PlugUSA):
        self.plug_usa = plug_usa

    def conectar(self) -> str:
        return self.plug_usa.connect()

# Cliente
def usar_carregador(plug: PlugUE):
    print(plug.conectar())

# Teste
if __name__ == "__main__":
    plug_europeu = PlugUE()
    usar_carregador(plug_europeu)

    print("---")

    plug_americano = PlugUSA()
    adaptador = AdaptadorUSAtoUE(plug_americano)
    usar_carregador(adaptador)
