# Padrão de Projeto: Chain of Responsibility

O padrão **Chain of Responsability (Corrente de Responsabilidade)** permite passar uma
requisição por uma **cadeia de objetos** até que um deles a trate. Cada objeto da cadeia
decide se **lida com a requisição** ou a **passa adiante**.

Ideal quando você quer que **vários objetos tenham a chance de processar uma requisição**, sem
que o emissor precise saber quem fará isso.

## Intenção

Evitar acoplamento entre rementente e receptor, permitindo que múltiplos objetos possam
**tratar uma requisição de forma flexível**.

## Estrutura

### Participantes:

- **Handler (Manipulador)**: interface comum para processar a requisição e encadear o próximo.
- **ConcreteHandler**: trata ou passa a requisição adiante.
- **Client (Cliente)**: envia a requisição para o primeiro handler da cadeia.

## Exemplo em Python

Vamos criar um sistema de **suporte técnico** com níveis diferentes: Atendente, Supervisor e 
Gerente. A requisição de atendimento sobe a cadeia conforme a complexidade.

```py
from abc import ABC, abstractmethod

# Handler base
class Suporte(ABC):
    def __init__(self):
        self._proximo = None

    def definir_proximo(self, proximo):
        self._proximo = proximo
        return proximo

    @abstractmethod
    def tratar(self, problema: str):
        pass

# Manipuladores concretos
class Atendente(Suporte):
    def tratar(self, problema: str):
        if problema == "senha":
            print("🔧 Atendente: Resolvi o problema de senha.")
        elif self._proximo:
            print("↪️ Atendente: Encaminhando para o Supervisor...")
            self._proximo.tratar(problema)
        else:
            print("❌ Atendente: Não consigo resolver.")

class Supervisor(Suporte):
    def tratar(self, problema: str):
        if problema == "rede":
            print("🛠️ Supervisor: Resolvi o problema de rede.")
        elif self._proximo:
            print("↪️ Supervisor: Encaminhando para o Gerente...")
            self._proximo.tratar(problema)
        else:
            print("❌ Supervisor: Não consigo resolver.")

class Gerente(Suporte):
    def tratar(self, problema: str):
        if problema == "servidor":
            print("🚨 Gerente: Resolvi o problema no servidor.")
        else:
            print("❌ Gerente: Problema não identificado.")

# Cliente
if __name__ == "__main__":
    atendente = Atendente()
    supervisor = Supervisor()
    gerente = Gerente()

    atendente.definir_proximo(supervisor).definir_proximo(gerente)

    print("\nChamado: problema com senha")
    atendente.tratar("senha")

    print("\nChamado: problema de rede")
    atendente.tratar("rede")

    print("\nChamado: problema no servidor")
    atendente.tratar("servidor")

    print("\nChamado: problema desconhecido")
    atendente.tratar("hack")
```

## Vantagens

- Desacopla o emissor do receptor
- Facilita adição/remoção de etapas da cadeia
- Permite implementar **filtros, validações, middleware** e mais

## Desvantagens

- Pode ser difícil de rastrear o caminho de execução
- Pode causar lentidão se a cadeia for longa ou mal otimizada

## Quando usar?

- Quando mais de um objeto pode tratar a requisição
- Quando os receptores devem ser definidos **em tempo de execução**
- Quando deseja evitar acoplamento direto entre rementente e receptores

## Exemplos de uso real

- Filtros HTTP (middlewares)
- Sistema de autorização
- Logging
- Manipuladores de eventos no frontend

## Referência
[Refactoring Guru – Chain of Responsibility](https://refactoring.guru/pt-br/design-patterns/chain-of-responsibility)