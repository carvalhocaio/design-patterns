from abc import ABC, abstractmethod

# Interface comum
class FileSystemComponent(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def exibir(self, indent=0): pass

# Folha
class Arquivo(FileSystemComponent):
    def exibir(self, indent=0):
        print("  " * indent + f"📄 {self.nome}")

# Composto
class Pasta(FileSystemComponent):
    def __init__(self, nome):
        super().__init__(nome)
        self._itens = []

    def adicionar(self, componente: FileSystemComponent):
        self._itens.append(componente)

    def exibir(self, indent=0):
        print("  " * indent + f"📁 {self.nome}")
        for item in self._itens:
            item.exibir(indent + 1)

# Cliente
if __name__ == "__main__":
    raiz = Pasta("root")

    pasta_docs = Pasta("Documentos")
    pasta_docs.adicionar(Arquivo("curriculo.pdf"))
    pasta_docs.adicionar(Arquivo("contrato.docx"))

    pasta_imagens = Pasta("Imagens")
    pasta_imagens.adicionar(Arquivo("foto1.png"))
    pasta_imagens.adicionar(Arquivo("logo.svg"))

    raiz.adicionar(pasta_docs)
    raiz.adicionar(pasta_imagens)
    raiz.adicionar(Arquivo("README.md"))

    raiz.exibir()
