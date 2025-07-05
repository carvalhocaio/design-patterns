# Padrão de Projeto: Iterator

O padrão **Iterator** fornece uma maneira de **acessar sequencialmente os elementos de uma coleção**,
sem expor sua representação interna (como listas, árvores, grafos, etc).

Ideal quando você quer **percorrer uma estrutura de dados complexa** de forma padronizada, sem
acoplamento com a estrutura.

## Intenção

Permitir que objetos de uma coleção sejam **percorridos um por um**, de forma uniforme, 
**sem conhecer a implementação interna** da coleção.

## Estrutura

### Participantes:

- **Iterator (Iterador)**: interface para percorrer elementos (`has_next()`, `next()`).
- **ConcreteIterator**: implementação específica do iterador.
- **Aggregate (Coleção)**: interface para criar iteradores.
- **ConcreteAggregate**: classe da coleção real.
- **Client**: usa o iterador sem conhecer a estrutura interna.

## Exemplo em Python

Vamos modelar uma coleção de **nomes de funcionários** que pode ser percorrida por um
iterador personalizado.

```py
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
```

> Nota: Python já suporta o protocolo de iteração nativamente com `__iter__()` e
`__next__()`, então esse padrão é **embutido na linguagem**.

## Vantagens

- Permite percorrer coleções sem acoplamento com sua estrutura
- Suporta múltiplas iterações simultâneas
- Pode implementar **filtros, ordens personalizadas** e **navegação reversa**

## Desvantagens

- Pode aumentar a complexidade para estruturas muito simples
- Requer mais código se a linguagem não suportar iteração nativamente

## Quando usar?

- Quando quer **iterar sobre uma coleção complexa**
- Quando precisa de **mais de uma forma de percorrer** os dados
- Quando precisa padronizar o acesso a diferentes tipos de coleções

## Comparações

Padrão    | Foco
--------- | ----------------------------
Iterator  | Navegar por uma coleção
Composite | Estrutura em árvore
Visitor   | Executar ações nos elementos

## Referência
[Refactoring Guru – Iterator](https://refactoring.guru/pt-br/design-patterns/iterator)