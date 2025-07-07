# Padrão de Projeto: Observer

O padrão **Observer** define uma **dependência de um-para-muitos** entre objetos,
onde quando um objeto muda de estado, todos os seus **observadores** são notificados
automaticamente.

Ideal quando você quer que **mútiplos objetos reajam** a eventos ou mudanças de
estado de outro objeto.

## Intenção

Permitir que um objeto **notifique automaticamente** outros objetos **interessados**
em seus eventos, **sem acoplamento direto** entre eles.

## Estrutura

## Participantes:

- **Subject (Sujeito)**: objeto observado que mantém a lista de observadores e os
notifica.
- **Observer (Observador)**: interface que define o método `atualizar()`.
- **ConcreteSubject**: objeto observador real.
- **ConcreteObserver**: classes que reagem à mudança do `Subject`.

## Exemplo em Python

Vamos simular um sistema de **alertas meteorológicos**, onde usuários se inscrevem
para receber notificações de clima.

```py
from abc import ABC, abstractmethod

# Observer
class Observador(ABC):
    @abstractmethod
    def atualizar(self, clima: str):
        pass

# Subject
class EstacaoClimatica:
    def __init__(self):
        self._observadores = []
        self._clima = None

    def adicionar(self, observador: Observador):
        self._observadores.append(observador)

    def remover(self, observador: Observador):
        self._observadores.remove(observador)

    def notificar(self):
        for observador in self._observadores:
            observador.atualizar(self._clima)

    def setar_clima(self, clima: str):
        print(f"\n📡 Estação: novo clima detectado: {clima}")
        self._clima = clima
        self.notificar()

# Observadores concretos
class AlertaSMS(Observador):
    def atualizar(self, clima: str):
        print(f"📱 SMS: Atenção! Clima atual: {clima}")

class AlertaEmail(Observador):
    def atualizar(self, clima: str):
        print(f"📧 Email: Aviso meteorológico: {clima}")

# Cliente
if __name__ == "__main__":
    estacao = EstacaoClimatica()

    sms = AlertaSMS()
    email = AlertaEmail()

    estacao.adicionar(sms)
    estacao.adicionar(email)

    estacao.setar_clima("Tempestade")
    estacao.setar_clima("Sol forte")
```

## Vantangens

- Segue o princípio **aberto/fechado**: é fácil adicionar/remover observadores
- Suporta **eventos desacoplados**
- Útil para **event-driven**, interfaces gráficas, notificações, etc.

## Desavantagens

- Pode causar **efeitos colaterais inesperados** se os observadores forem mal
implementados
- Ordem de notificação pode ser incerta
- Pode gerar **vazamento de memória** se observadores não forem removidos

## Quando usar?

- Quando você precisa que **múltiplos objetos reajam** a uma mudança em outro
- Quando quer **desacoplar** quem emite eventos de quem reage
- Quando implementam **sistemas de publicação/assinatura (pub/sub)**

## Exemplos reais

- Interfaces gráficas (ex: botão -> evento de clique)
- Stream dados
- Sistemas de **notificação** (como webhooks)
- **Bindings** em React, Angular, Vue

## Referência
[Refactoring Guru – Observer](https://refactoring.guru/pt-br/design-patterns/observer)
