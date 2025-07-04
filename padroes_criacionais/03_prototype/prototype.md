# Padrão de Projeto: Prototype

O padrão **Prototype** permite copiar objetos existentes sem depender de suas classes
concretas. Ele é útil quando a criação de um novo objeto do zero é **custosa ou complexa**, e
é mais fácil **clonar** um já existente.

Ideal quando você precisa de muitas **instâncias semelhantes** com pequenas variações.

## Intenção

Criar novos objetos a partir de **protótipos** (modelos) atráves da clonagem, mantendo a
independência de suas classes concretas.

## Estrutura

### Participantes principais

- **Prototype (Protótipo)**: interface com o método `clone`.
- **ConcretePrototype (Protótipos Concretos)**: implementam a clonagem.
- **Client (Cliente)**: clona objetos via `clone()` em vez de usar `new`.

## Exemplo em Python

Python facilita esse padrão com o módulo `copy`.

### Exemplo: Documentos de um editor gráfico

```py
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
```

## Vantagens

- Criação de objetos é mais rápida (evita construção do zero)
- Reduz acoplamento com classes concretas
- Útil para objetos com estrutura complexa ou configuração inicial cara

## Desvantagens

- Cópia profunda pode ser custosa ou difícil de manter
- Clonagem de objetos com referências complexas pode gerar bugs sutis

## Quando usar?

- Quando os objetos são **caros de criar**
- Quando quer evitar subclasses para configurar objetos
- Quando precisa de muitas cópias com pequenas variações

## Referência
[Refactoring Guru - Prototype](https://refactoring.guru/pt-br/design-patterns/prototype)