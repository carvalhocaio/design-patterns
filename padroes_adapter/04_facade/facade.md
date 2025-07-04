# Padrão de Projeto: Facade

O padrão **Facade** fornece uma interface **simplificada** e unificada para um conjunto de
interfaces em um subsistema, tornando o subsistema mais fácil de usar.

Ideal quando você quer **esconder a complexidade** de várias classes e expor uma interface
mais amigável ao cliente.

## Intenção

Reduzir o acoplamento entre cliente e subsistema, fornecendo um ponto de entrada único para
diversas funcionalidades internas.

## Estrutura

### Participantes:

- **Facade**: classe que oferece métodos de alto nível e delega chamadas para o subsistema.
- **Subsystem Classes (Subsistema)**: classes que fazem o trabalho real, mas que o cliente
não precisa conhecer diretamente.
- **Client (Cliente)**: interage com a Facade, sem se preocupar com os detalhes do subsistema.

## Exemplo em Python

Vamos modelar um sistema de **home theater**, com vários componentes (TV, som, luzes), 
controlados por uma única fachada.

```py
# Subsistema
class Luz:
    def ligar(self):
        print("💡 Luzes acesas")

    def desligar(self):
        print("💡 Luzes apagadas")

class TV:
    def ligar(self):
        print("📺 TV ligada")

    def desligar(self):
        print("📺 TV desligada")

class Som:
    def ligar(self):
        print("🔊 Som ligado")

    def desligar(self):
        print("🔇 Som desligado")

# Facade
class HomeTheaterFacade:
    def __init__(self, luz: Luz, tv: TV, som: Som):
        self.luz = luz
        self.tv = tv
        self.som = som

    def assistir_filme(self):
        print("🎬 Preparando sessão de cinema...")
        self.luz.desligar()
        self.som.ligar()
        self.tv.ligar()

    def encerrar_filme(self):
        print("🛑 Encerrando sessão de cinema...")
        self.tv.desligar()
        self.som.desligar()
        self.luz.ligar()

# Cliente
if __name__ == "__main__":
    luz = Luz()
    tv = TV()
    som = Som()

    home_theater = HomeTheaterFacade(luz, tv, som)

    home_theater.assistir_filme()
    print("\n---\n")
    home_theater.encerrar_filme()
```

## Vantagens

- Esconde a complexidade do sistema
- Reduz o acoplamento entre cliente e classes internas
- Facilita o uso e a manutenção

## Desvantagens

- Pode se tornar um "Deus Objeto" se crescer demais
- Esconde funcionalidades avançadas do subsistema (se mal projetado)

## Quando usar?

- Quando você tem um sistema com **muitas classes interdependentes**
- Quando deseja **padronizar o ponto de acesso** a subsistemas
- Quando quer que o código cliente seja mais **limpo e legível**

## Facade vs Adapter

Ponto                | Facade                    | Adapter
-------------------- | ------------------------- | -------------------------------------
Foco                 | Simplicidade de uso       | Compatibilizar interfaces
Criação              | Normalmente você que cria | Normalmente é criado para algo legado
Complexidade interna | Esconde                   | Traduz

## Referência
[Refactoring Guru – Facade](https://refactoring.guru/pt-br/design-patterns/facade)