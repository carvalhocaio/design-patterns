# Padrão de Projeto: Template Method

O padrão **Template Method** define o **esqueleto de um algoritmo** em uma classe base,
deixando **algumas etapas para subclasses implementarem**. Assim, o algoritmo geral
permanece o mesmo, mas certos detalhes podem ser personalizados.

Ideal quando você tem **um processo com passos fixos**, mas que precisa ser parcialmente
customizado por subclasses.

## Intenção

Permitir que subclasses redefinam certas etapas de um algoritmo **sem alterar sua estrutura geral**.

## Estrutura

### Participantes:

- **AbstractClass**: define o **template method**, que organiza o algoritmo e chama os
métodos abstratos ou ganchos (`hooks`).
- **ConcreteClass**: implementa os métodos específicos da lógica que pode variar.

## Exemplo em Python

Vamos simular o processo de **preparar uma bebida quente**, como chá, ou café. A estrutura geral
é igual, mas algumas etapas variam.

```py
from abc import ABC, abstractmethod

# Classe abstrata com o Template Method
class BebidaQuente(ABC):
    def preparar(self):
        self.esquentar_agua()
        self.adicionar_principal()
        self.adicionar_acompanhamentos()
        self.servir()

    def esquentar_agua(self):
        print("🔥 Esquentando água...")

    @abstractmethod
    def adicionar_principal(self):
        pass

    @abstractmethod
    def adicionar_acompanhamentos(self):
        pass

    def servir(self):
        print("🥤 Servindo bebida...\n")

# Subclasses concretas
class Cha(BebidaQuente):
    def adicionar_principal(self):
        print("🍃 Adicionando folhas de chá...")

    def adicionar_acompanhamentos(self):
        print("🍋 Adicionando limão...")

class Cafe(BebidaQuente):
    def adicionar_principal(self):
        print("☕ Adicionando pó de café...")

    def adicionar_acompanhamentos(self):
        print("🥄 Adicionando açúcar...")

# Cliente
if __name__ == "__main__":
    print("Preparando chá:")
    bebida = Cha()
    bebida.preparar()

    print("Preparando café:")
    bebida = Cafe()
    bebida.preparar()
```

## Vantagens

- **Evita duplicação** de lógica comum
- Segue o princípio **aberto/fechado**: permite alteração sem mudar a estrutura
- Força uma estrutura **consistente** em todas as implementações

## Desvantagens

- Reduz flexibilidade (uso fixo de herança em vez de composição)
- Pode tornar a hierarquia de classes complexa

## Quando usar?

- Quando várias classes seguem **a mesma lógica geral** com **algumas variações**
- Quando quer **forçar uma ordem de execução**
- Quando quer promover **reutilização de código base**

## Comparações

Padrão          | Propósito
--------------- | ---------------------------------------------------
Template Method | Define estrutura fixa, delega partes para subclasse
Strategy        | Algoritmo inteiro é intercambiável via composição
Observer        | Reage a eventos, não define estrutura de execução

## Referência
[Refactoring Guru – Template Method](https://refactoring.guru/pt-br/design-patterns/template-method)