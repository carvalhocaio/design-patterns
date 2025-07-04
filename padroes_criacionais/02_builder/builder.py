from abc import ABC, abstractmethod

# Produto final
class Lanche:
    def __init__(self):
        self.itens = []

    def adicionar(self, item: str):
        self.itens.append(item)

    def mostrar(self):
        print("Lanche inclui:")
        for item in self.itens:
            print(f" - {item}")

# Builder (interface)
class LancheBuilder(ABC):
    @abstractmethod
    def adicionar_pao(self): pass

    @abstractmethod
    def adicionar_carne(self): pass

    @abstractmethod
    def adicionar_bebida(self): pass

    @abstractmethod
    def obter_lanche(self) -> Lanche: pass

# ConcreteBuilder
class LancheCheddarBuilder(LancheBuilder):
    def __init__(self):
        self.lanche = Lanche()

    def adicionar_pao(self):
        self.lanche.adicionar("Pão de brioche")

    def adicionar_carne(self):
        self.lanche.adicionar("Hambúrguer de carne com cheddar")

    def adicionar_bebida(self):
        self.lanche.adicionar("Refrigerante")

    def obter_lanche(self) -> Lanche:
        return self.lanche

# Outro Builder
class LancheVeganoBuilder(LancheBuilder):
    def __init__(self):
        self.lanche = Lanche()

    def adicionar_pao(self):
        self.lanche.adicionar("Pão integral")

    def adicionar_carne(self):
        self.lanche.adicionar("Hambúrguer de grão-de-bico")

    def adicionar_bebida(self):
        self.lanche.adicionar("Suco natural")

    def obter_lanche(self) -> Lanche:
        return self.lanche

# Diretor (opcional)
class Diretor:
    def __init__(self, builder: LancheBuilder):
        self._builder = builder

    def construir_lanche_completo(self):
        self._builder.adicionar_pao()
        self._builder.adicionar_carne()
        self._builder.adicionar_bebida()

# Cliente
if __name__ == "__main__":
    builder = LancheVeganoBuilder()
    diretor = Diretor(builder)
    diretor.construir_lanche_completo()

    lanche = builder.obter_lanche()
    lanche.mostrar()

    print("\n---\n")

    builder2 = LancheCheddarBuilder()
    diretor = Diretor(builder2)
    diretor.construir_lanche_completo()

    lanche2 = builder2.obter_lanche()
    lanche2.mostrar()
