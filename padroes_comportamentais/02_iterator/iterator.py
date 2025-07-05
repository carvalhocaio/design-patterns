# Iterator
class FuncionarioIterator:
    def __init__(self, funcionarios):
        self._funcionarios = funcionarios
        self._posicao = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._posicao < len(self._funcionarios):
            nome = self._funcionarios[self._posicao]
            self._posicao += 1
            return nome
        else:
            raise StopIteration

# Coleção
class Departamento:
    def __init__(self):
        self._funcionarios = []

    def adicionar(self, nome):
        self._funcionarios.append(nome)

    def __iter__(self):
        return FuncionarioIterator(self._funcionarios)

# Cliente
if __name__ == "__main__":
    ti = Departamento()
    ti.adicionar("Alice")
    ti.adicionar("Bruno")
    ti.adicionar("Carla")

    print("Funcionários do TI:")
    for funcionario in ti:
        print(f"👤 {funcionario}")
