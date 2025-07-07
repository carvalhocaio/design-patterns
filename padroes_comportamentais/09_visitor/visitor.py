from abc import ABC, abstractmethod

# Visitor
class Visitor(ABC):
    @abstractmethod
    def visitar_arquivo(self, arquivo): pass

    @abstractmethod
    def visitar_pasta(self, pasta): pass

# Element
class Elemento(ABC):
    @abstractmethod
    def aceitar(self, visitor: Visitor): pass

# Elementos concretos
class Arquivo(Elemento):
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho

    def aceitar(self, visitor: Visitor):
        visitor.visitar_arquivo(self)

class Pasta(Elemento):
    def __init__(self, nome):
        self.nome = nome
        self.conteudo = []

    def adicionar(self, elemento: Elemento):
        self.conteudo.append(elemento)

    def aceitar(self, visitor: Visitor):
        visitor.visitar_pasta(self)

# Visitor concreto
class CalculadoraTamanho(Visitor):
    def __init__(self):
        self.total = 0

    def visitar_arquivo(self, arquivo: Arquivo):
        print(f"📄 Arquivo: {arquivo.nome} ({arquivo.tamanho} KB)")
        self.total += arquivo.tamanho

    def visitar_pasta(self, pasta: Pasta):
        print(f"📁 Pasta: {pasta.nome}")
        for item in pasta.conteudo:
            item.aceitar(self)

# Cliente
if __name__ == "__main__":
    raiz = Pasta("Documentos")
    raiz.adicionar(Arquivo("cv.pdf", 300))
    raiz.adicionar(Arquivo("foto.jpg", 1500))

    subpasta = Pasta("Projetos")
    subpasta.adicionar(Arquivo("app.py", 40))
    subpasta.adicionar(Arquivo("readme.md", 10))
    raiz.adicionar(subpasta)

    calculadora = CalculadoraTamanho()
    raiz.aceitar(calculadora)

    print(f"\n📦 Tamanho total: {calculadora.total} KB")
