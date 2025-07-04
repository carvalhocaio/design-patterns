import copy
from abc import ABC, abstractmethod

# Interface do protótipo
class Documento(ABC):
    def __init__(self, titulo: str, conteudo: str):
        self.titulo = titulo
        self.conteudo = conteudo

    @abstractmethod
    def clone(self):
        pass

# Protótipo concreto
class DocumentoTexto(Documento):
    def __init__(self, titulo: str, conteudo: str, fonte: str = "Arial"):
        super().__init__(titulo, conteudo)
        self.fonte = fonte

    def clone(self):
        return copy.deepcopy(self)

    def exibir(self):
        print(f"Documento: {self.titulo}")
        print(f"Fonte: {self.fonte}")
        print(f"Conteúdo: {self.conteudo}")

# Cliente
if __name__ == "__main__":
    original = DocumentoTexto("Relatório", "Dados do projeto...", "Helvetica")
    copia = original.clone()

    copia.titulo = "Relatório - Cópia"
    copia.fonte = "Times New Roman"

    original.exibir()
    print("\n---\n")
    copia.exibir()
