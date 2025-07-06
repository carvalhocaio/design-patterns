# Padrão de Projeto: Memento

O padrão **Memento** permite capturar e armazenar o **estado interno de um objeto** para
que ele possa ser restaurado posteriormente, **sem expor os detalhes internos da sua implementação**.

Ideal quando você precisa de **desfazer/refazer**, ou implementar um **histórico de alterações**.

## Intenção

Permitir salvar o estado de **snapshot (memento)** e restaurá-lo mais tarde, mantendo
**encapsulamento total**;

## Estrutura

### Participantes:

- **Originator**: o objeto cujo estado será salvo.
- **Memento**: o snapshot imutável do estado.
- **Caretaker**: armazena e gerencia os mementos, sem modificar seu conteúdo.

## Exemplo em Python

Vamos simular um **editor de texto simples**, com suporte a **desfazer** (`undo`).

```py
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
```

## Vantagens

- Permite **desfazer/refazer** sem violar o encapsulamento
- Pode manter **histórico de versões**
- Cliente (Caretaker) não precisa saber dos detalhes internos do objeto

## Desvantagens

- Pode consumir muita **memória** se os mementos forem grandes ou frquentes
- O **Carataker** precisa gerenciar o histórico manualmente

## Quando usar?

- Quando precisa de **funcionalidade de desfazer**
- Quando quer implementar **histórico, checkpoint ou rollback**
- Quando precisa **preservar o encapsulamento**

## Comparações

Padrão | Finalidade
------ | ----------
Memento | Armazenar/restaurar estados
Command | Executar/desfazer ações
Snapshot | Estrutura de dados (sem lógica)

## Referência
[Refactoring Guru – Memento](https://refactoring.guru/pt-br/design-patterns/memento)