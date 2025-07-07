# Padrão de Projeto: Visitor

O padrão **Visitor** permite adicionar **novas operações a uma estrutura de objetos existente**
sem modificar as classes desses objetos. Ele separa a **lógica de operação** da
**estrutura dos dados**.

Ideal quando você quer aplicar diferentes **ações** a objetos de **vários tipos diferentes**
dentro de uma estrutura (como árvores, listas, gráficos).

## Intenção

Permitir que novas operações sejam adicionados a objetos de uma estrutura de forma desacoplada,
sem alterar as classes dos objetos.

## Estrutura

### Participantes:

- **Visitor**: interface que declara uma operação para cada tipo de elemento.
- **ConcreteVisitor**: implementa ações específicas para cada tipo.
- **Element**: interface que declara `accept(visitor)`.
- **ConcreteElement**: implementa o método `accept`, chamando o método do visitante correspondente.
- **Client**: percorre os elementos e aplica o visitante.

## Exemplo em Python

Vamos criar um exemplo com uma estrutura de arquivos (pastas e arquivos), e um visitante
que **calcula o tamanho total**.

```py
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
```

## Vantagens

- Facilita a **adição de comportamentos** a estruturas existentes
- Segue o princípio **aberto/fechado** (abrir para extensão, fechar para modificação)
- Permite **operar sobre diferentes tipos** em um estrutura heterogênea

## Desvantagens

- Depende de **double dispatch** (pode parecer "indireto")
- Quebra o encapsulamento se mal usado
- Pode ser **complexo** para estruturas mutáveis ou altamente dinâmicas

## Quando usar?

- Quando precisa aplicar várias operações distintas a objetos em uma estrutura complexa
- Quando quer **separar lógica de negócios da estrutura de dados**
- Quando precisa **percorrer estruturas com tipos diversos**

## Comparações

Padrão    | Propósito
--------- | ----------------------------------------------
Visitor   | Aplicar operações externas a objetos variados
Strategy  | Trocar algoritmos em tempo de execução
Template  | Fixar estrutura, personalizar partes
Composite | Trabalhar com objetos em estrutura hierárquica

## Referência
[Refactoring Guru – Visitor](https://refactoring.guru/pt-br/design-patterns/visitor)