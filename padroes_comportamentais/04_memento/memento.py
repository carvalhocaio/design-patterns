# Memento
class EditorMemento:
    def __init__(self, texto):
        self._texto = texto

    def get_texto(self):
        return self._texto

# Originator
class EditorTexto:
    def __init__(self):
        self._texto = ""

    def digitar(self, texto):
        self._texto += texto

    def exibir(self):
        print(f"📝 Texto atual: {self._texto}")

    def salvar(self):
        return EditorMemento(self._texto)

    def restaurar(self, memento: EditorMemento):
        self._texto = memento.get_texto()

# Caretaker
class Historico:
    def __init__(self):
        self._estados = []

    def salvar_estado(self, memento: EditorMemento):
        self._estados.append(memento)

    def desfazer(self):
        if self._estados:
            return self._estados.pop()
        return None

# Cliente
if __name__ == "__main__":
    editor = EditorTexto()
    historico = Historico()

    editor.digitar("Olá")
    historico.salvar_estado(editor.salvar())

    editor.digitar(", mundo!")
    historico.salvar_estado(editor.salvar())

    editor.exibir()

    print("\n🔙 Desfazendo...")
    editor.restaurar(historico.desfazer())
    editor.exibir()

    print("\n🔙 Desfazendo novamente...")
    editor.restaurar(historico.desfazer())
    editor.exibir()
