# Padrão de Projeto: Command

O padrão **Command** transforma **uma solicitação em um objeto**, permitindo:

- Que você armazene, desfaça ou refaça comandos
- Que o remetente e o receptor fiquem **desacoplados**
- Que comandos sejam enfileirados, registrados ou logados

Ideal para **controle de ações**, como desfazer/refazer, automação, ou execução agendada.

## Intenção

Encapsular uma solicitação como objeto, permitindo
**parametrização de métodos, adiamento de execução, registro, log** e **desfazer/refazer**.

## Estrutura

### Participantes

- **Command**: interface com o método `executar()`.
- **ConcreteCommand**: implementação que chama o método de um receptor.
- **Receiver**: classe que realiza a ação de fato.
- **Invoker**: objeto que chama o comando.
- **Client**: configura os comandos e liga com o invocador.

## Exemplo em Python

Vamos modelar um **contole remoto** que pode ligar e desligar luzes por meio de comandos.

```py
from abc import ABC, abstractmethod

# Receiver (quem executa as ações reais)
class Luz:
    def ligar(self):
        print("💡 Luz ligada")

    def desligar(self):
        print("💡 Luz desligada")

# Command
class Comando(ABC):
    @abstractmethod
    def executar(self): pass

# Concrete Commands
class LigarLuz(Comando):
    def __init__(self, luz: Luz):
        self.luz = luz

    def executar(self):
        self.luz.ligar()

class DesligarLuz(Comando):
    def __init__(self, luz: Luz):
        self.luz = luz

    def executar(self):
        self.luz.desligar()

# Invoker
class ControleRemoto:
    def __init__(self):
        self._historico = []

    def executar_comando(self, comando: Comando):
        self._historico.append(comando)
        comando.executar()

# Cliente
if __name__ == "__main__":
    luz_sala = Luz()

    comando_ligar = LigarLuz(luz_sala)
    comando_desligar = DesligarLuz(luz_sala)

    controle = ControleRemoto()
    controle.executar_comando(comando_ligar)
    controle.executar_comando(comando_desligar)
```

## Vantagens

- **Desacopla** o objeto que emite a ação do objeto que a executa
- Permite **desfazer/refazer**
- Suporta **log, fila de comandos**, e execução **em lote**
- Permite construção de **macros** (vários comandos agrupados)

## Desvantagens

- Pode aumentar o número de classes
- Overhead para ações simples

## Quando usar?

- Quando quer **parametrizar objetos com ações**
- Quando precisa de **fila, log, histórico ou macro**,
- Quando deseja **desacoplar remetente de receptor**

## Exemplos reais

- Interfaces gráficas (menus, botões)
- Sistemas de automação
- Comandos do shell
- Operações de desfazer/refazer

## Referência
[Refactoring Guru – Command](https://refactoring.guru/pt-br/design-patterns/command)