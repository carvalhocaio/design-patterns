# Padrão de Projeto: Bridge

O padrão **Bridge** desacopla uma abstração de sua implementação, de modo que as duas possam
**variar independemente**.

Ideal quando você tem **múltiplas variantes de abstrações e implementações**, e não quer
uma explosão de subclasses para cobrir todas as combinações.

## Intenção

Evitar que mudanças na **abstração** impactem diretamente na **implementação**
e vice-versa. Em vez de herança, usa-se **composição** para separar as camadas.

## Estrutura

### Participantes

- **Abstraction (Abstração)**: interface de alto nível que usa a implementação.
- **RefinedAbstraction**: variação da abstração, que pode adicionar comportamento extra.
- **Implementor (Implementador)**: interface comum das implementações.
- **ConcreteImplementor**: implementações concretas do `Implementor`.

## Exemplo em Python

Vamos criar um sistam de **controle remoto** que pode funcionar
com **TVs de diferentes marcas** (Samsung, LG), sem acoplar o controle à marca.

```py
from abc import ABC, abstractmethod

# Implementador
class Dispositivo(ABC):
    @abstractmethod
    def ligar(self): pass

    @abstractmethod
    def desligar(self): pass

# Implementações concretas
class TVSamsung(Dispositivo):
    def ligar(self):
        print("TV Samsung ligada.")

    def desligar(self):
        print("TV Samsung desligada.")

class TVLG(Dispositivo):
    def ligar(self):
        print("TV LG ligada.")

    def desligar(self):
        print("TV LG desligada.")

# Abstração
class ControleRemoto:
    def __init__(self, dispositivo: Dispositivo):
        self.dispositivo = dispositivo

    def ligar(self):
        self.dispositivo.ligar()

    def desligar(self):
        self.dispositivo.desligar()

# Abstração refinada
class ControleRemotoAvancado(ControleRemoto):
    def silenciar(self):
        print("Dispositivo silenciado (modo mudo).")

# Cliente
if __name__ == "__main__":
    tv_samsung = TVSamsung()
    controle_samsung = ControleRemotoAvancado(tv_samsung)
    controle_samsung.ligar()
    controle_samsung.silenciar()
    controle_samsung.desligar()

    print("\n---\n")

    tv_lg = TVLG()
    controle_lg = ControleRemoto(tv_lg)
    controle_lg.ligar()
    controle_lg.desligar()
```

## Vantagens

- Separa claramente **interface** de **implementação**
- Reduz número de subclasses necessárias
- Facilita evolução e manutenção da cada parte

## Desvantagens

- Introduz mais classes a abstrações
- Pode complicar projetos simples se usado desnecessariamente

## Quando usar?

- Quando deseja evitar explosão de subclasses para combinar diferentes variantes
- Quando abstrações e implementações devem evoluir de forma independente
- Quando classes precisam trocar de implementações em tempo de execução

## Comparação com Adapter

Ponto              | Bridge                            | Adapter
-------------------| --------------------------------- | -------------------------------
Intenção           | Separar abstração e implementação | Adaptar interface incompatível
Aplicação          | Projetos novos/modularização      | Integração com sistemas legados
Direção de ligação | Composição                        | Composição (ou herança)

## Referência
[Refactoring Guru – Bridge](https://refactoring.guru/pt-br/design-patterns/bridge)