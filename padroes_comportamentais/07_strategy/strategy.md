# Padrão de Projeto: Strategy

O padrão **Strategy** define uma **família de algoritmos**, encapsula cada um deles e os torna
intercambiáveis. O algoritmo pode variar **independentemente dos clientes que o utilizam**.

Ideal quando você tem **várias formas de executar uma tarefa** e quer poder
**trocar de estratégia em tempo de execução**.

## Intenção

Permitir que o algoritmo usado por um objeto seja **alterado em tempo de execução**, delegando
o comportamento a um objeto "estratégia".

## Estrutura

### Participantes

- **Strategy**: interface comum para todas as estratégias.
- **ConcreteStrategy**: implementações específicas do algoritmo.
- **Context**: utiliza uma instância de Strategy e a delega o comportamento.

## Exemplo em Python

Vamos criar um exemplo de **ordenação de listas**, onde podemos escolher a estratégia de
ordenação (crescente, decrescente, por tamanho de string).

```py
from abc import ABC, abstractmethod

# Strategy
class EstrategiaOrdenacao(ABC):
    @abstractmethod
    def ordenar(self, lista: list):
        pass

# Concrete Strategies
class OrdenarCrescente(EstrategiaOrdenacao):
    def ordenar(self, lista: list):
        return sorted(lista)

class OrdenarDecrescente(EstrategiaOrdenacao):
    def ordenar(self, lista: list):
        return sorted(lista, reverse=True)

class OrdenarPorTamanho(EstrategiaOrdenacao):
    def ordenar(self, lista: list):
        return sorted(lista, key=len)

# Contexto
class ListaPalavras:
    def __init__(self, estrategia: EstrategiaOrdenacao):
        self._estrategia = estrategia
        self._palavras = []

    def adicionar(self, palavra: str):
        self._palavras.append(palavra)

    def definir_estrategia(self, estrategia: EstrategiaOrdenacao):
        self._estrategia = estrategia

    def exibir(self):
        resultado = self._estrategia.ordenar(self._palavras)
        print("📝 Lista ordenada:", resultado)

# Cliente
if __name__ == "__main__":
    lista = ListaPalavras(OrdenarCrescente())
    lista.adicionar("banana")
    lista.adicionar("maçã")
    lista.adicionar("abacaxi")

    print("Estratégia: crescente")
    lista.exibir()

    print("\nEstratégia: por tamanho")
    lista.definir_estrategia(OrdenarPorTamanho())
    lista.exibir()

    print("\nEstratégia: decrescente")
    lista.definir_estrategia(OrdenarDecrescente())
    lista.exibir()
```

## Vantagens

- Facilita a **substituição de algoritmos em tempo de execução**
- Segue o princípio de **aberto/fechado** (novas estratégias sem alterar o código existente)
- Evita condicionais `if/else` para escolha de comportamentos

## Desvantagens

- Pode aumentar o número de classes
- O cliente precisa conhecer as estratégias disponíveis

## Quando usar?

- Quando precisa alternar entre **diferentes algoritmos ou lógicas**
- Quando quer evitar **condicionais múltiplas** para decidir o comportamento
- Quando deseja seguir o **princípio da responsabilidade única**

## Comparações

Padrão   | Finalidade
-------- | -----------------------------------------
Strategy | Selecionar algoritmo em tempo de execução
State    | Mudar comportamento baseado em estado
Command  | Encapsular ações como objetos

## Referência
[Refactoring Guru - Strategy](https://refactoring.guru/pt-br/design-patterns/strategy)