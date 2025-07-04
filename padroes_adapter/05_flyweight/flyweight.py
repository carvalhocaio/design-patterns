# Flyweight
class TipoArvore:
    def __init__(self, nome, cor, textura):
        self.nome = nome
        self.cor = cor
        self.textura = textura

    def renderizar(self, x, y):
        print(f"🌳 {self.nome} ({self.cor}, {self.textura}) em posição ({x},{y})")

# Flyweight Factory
class FabricaTiposArvore:
    _tipos = {}

    @classmethod
    def obter_tipo(cls, nome, cor, textura):
        chave = (nome, cor, textura)
        if chave not in cls._tipos:
            cls._tipos[chave] = TipoArvore(nome, cor, textura)
        return cls._tipos[chave]

# Contexto (estado extrínseco)
class Arvore:
    def __init__(self, x, y, tipo: TipoArvore):
        self.x = x
        self.y = y
        self.tipo = tipo

    def renderizar(self):
        self.tipo.renderizar(self.x, self.y)

# Cliente
class Floresta:
    def __init__(self):
        self.arvores = []

    def plantar_arvore(self, x, y, nome, cor, textura):
        tipo = FabricaTiposArvore.obter_tipo(nome, cor, textura)
        self.arvores.append(Arvore(x, y, tipo))

    def renderizar(self):
        for arvore in self.arvores:
            arvore.renderizar()

# Teste
if __name__ == "__main__":
    floresta = Floresta()
    floresta.plantar_arvore(1, 2, "Ipê", "Amarelo", "Lisa")
    floresta.plantar_arvore(3, 4, "Ipê", "Amarelo", "Lisa")
    floresta.plantar_arvore(5, 6, "Jacarandá", "Roxo", "Cascuda")

    floresta.renderizar()

    print("\nTotal de tipos únicos:", len(FabricaTiposArvore._tipos))
