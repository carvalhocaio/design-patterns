from abc import ABC, abstractmethod

# Strategy
class EstrategiaOrdenacao(ABC):
    @abstractmethod
    def ordenar(self, lista: list):
        pass

# Concrete Strategies
class OrdenarCrescente(EstrategiaOrdenacao):
    def ordenar(self, lista: list):
        return sorted(lista)

class OrdenarDecrescente(EstrategiaOrdenacao):
    def ordenar(self, lista: list):
        return sorted(lista, reverse=True)

class OrdenarPorTamanho(EstrategiaOrdenacao):
    def ordenar(self, lista: list):
        return sorted(lista, key=len)

# Contexto
class ListaPalavras:
    def __init__(self, estrategia: EstrategiaOrdenacao):
        self._estrategia = estrategia
        self._palavras = []

    def adicionar(self, palavra: str):
        self._palavras.append(palavra)

    def definir_estrategia(self, estrategia: EstrategiaOrdenacao):
        self._estrategia = estrategia

    def exibir(self):
        resultado = self._estrategia.ordenar(self._palavras)
        print("📝 Lista ordenada:", resultado)

# Cliente
if __name__ == "__main__":
    lista = ListaPalavras(OrdenarCrescente())
    lista.adicionar("banana")
    lista.adicionar("maçã")
    lista.adicionar("abacaxi")

    print("Estratégia: crescente")
    lista.exibir()

    print("\nEstratégia: por tamanho")
    lista.definir_estrategia(OrdenarPorTamanho())
    lista.exibir()

    print("\nEstratégia: decrescente")
    lista.definir_estrategia(OrdenarDecrescente())
    lista.exibir()
