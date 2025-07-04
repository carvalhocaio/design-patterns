# Padrão de Projeto: Composite

O padrão **Composite** permite tratar objetos individuais e **coleções de objetos** de maneira
uniforme, formando **estruturas em árvore** para representar hierarquias "parte-todo".

Ideal quando você quer que objetos **simples e compostos** compartilhem a mesma interface.

## Intenção

Permitir que o cliente trate **objetos individuais** e **estruturas compostas** (como listas de
objetos) da mesma forma, usando uma interface comum.

## Estrutura

### Participantes

- **Component (Componente)**: interface comum para folhas e compostos.
- **Leaf (Folha)**: representa objetos simples (não tem filhos).
- **Composite (Composto)**: contém filhos, que podem ser folhas ou outros compostos.
- **Client (Cliente)**: usa a interface `Component`.

## Exemplo em Python

Vamos modelar um **siste de arquivos**, com pastas e arquivos sendo tratados da mesma forma.

```py
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
```

## Vantagens

- Permite trabalhar com **estruturas recursivas** de forma elegante
- Facilita a **expansão de novos tipos de componentes**
- Código cliente pode operar de forma uniforme sobre todos os objetos

## Desvantagens

- Pode ser difícil restringir alguns tipos de componentes (ex: impedir que folhas
tenham filhos)
- Estrutura pode ficar complexa se houver muitos tipos diferentes de elementos

## Quando usar?

- Quando deseja **representar estruturas hierárquicas**
- Quando quer que objetos **simples e compostos** tenham **comportamento uniforme**
- Quando seu código cliente não deve se preocupar se está lidando com uma folha ou um composto

## Referência
[Refactoring Guru – Composite](https://refactoring.guru/pt-br/design-patterns/composite)