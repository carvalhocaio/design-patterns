from abc import ABC, abstractmethod

# Interface do Produto
class Transporte(ABC):
    @abstractmethod
    def entregar(self) -> str:
        pass

# Produtos Concretos
class Caminhao(Transporte):
    def entregar(self) -> str:
        return "Entrega feita por caminhão."

class Navio(Transporte):
    def entregar(self) -> str:
        return "Entrega feita por navio."

# Criador
class Logistica(ABC):
    @abstractmethod
    def criar_transporte(self) -> Transporte:
        pass

    def planejar_entrega(self) -> str:
        transporte = self.criar_transporte()
        return transporte.entregar()

# Criadores Concretos
class LogisticaRodoviaria(Logistica):
    def criar_transporte(self) -> Transporte:
        return Caminhao()

class LogisticaMaritima(Logistica):
    def criar_transporte(self) -> Transporte:
        return Navio()

# Cliente
def client_code(logistica: Logistica) -> None:
    print(logistica.planejar_entrega())

# Teste
if __name__ == "__main__":
    print("Usando logística rodoviária:")
    client_code(LogisticaRodoviaria())

    print("\nUsando logística marítima:")
    client_code(LogisticaMaritima())
