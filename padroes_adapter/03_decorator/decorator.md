# Padrão de Projeto: Decorator

O padrão **Decorator** permite adicionar **comportamento extra** a objetos de forma
**dinâmica**, sem alterar sua estrutura original, usando composição ao invés de herança.

Ideal quando você quer **encaixar funcionalidades extras** em objetos específicos sem impactar
os demais.

## Intenção

Anexar responsabilidades adicionais a um objeto **de forma dinâmica**, usando **decoradores**
que envolvem o objeto original.

## Estrutura

### Participantes:

- **Component (Componente)**: interface comum para objetos que podem ser decorados.
- **ConcreteComponent (Componente Concreto)**: implementação original do objeto
- **Decorator (Decorator Abstrato)**: possui referência ao componente e delega a ele.
- **ConcreteDecorator (Decorador Concreto)**: adiciona comportamento ao componente.

## Exemplo em Python

Vamos modelar um sistema de **notificações**, onde podemos adicionar **envio por e-mail, SMS**, 
ou outros canais de forma decorável.

```py
from abc import ABC, abstractmethod

# Interface do componente
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensagem: str):
        pass

# Componente concreto
class NotificadorBase(Notificador):
    def enviar(self, mensagem: str):
        print(f"📢 Notificando: {mensagem}")

# Decorador base
class NotificadorDecorator(Notificador):
    def __init__(self, wrappee: Notificador):
        self._wrappee = wrappee

    def enviar(self, mensagem: str):
        self._wrappee.enviar(mensagem)

# Decorador concreto - Email
class NotificadorEmail(NotificadorDecorator):
    def enviar(self, mensagem: str):
        super().enviar(mensagem)
        print(f"📧 Enviando e-mail: {mensagem}")

# Decorador concreto - SMS
class NotificadorSMS(NotificadorDecorator):
    def enviar(self, mensagem: str):
        super().enviar(mensagem)
        print(f"📱 Enviando SMS: {mensagem}")

# Cliente
if __name__ == "__main__":
    notificador_simples = NotificadorBase()
    print("Notificação simples:")
    notificador_simples.enviar("Sistema em manutenção")

    print("\nNotificação com e-mail:")
    notificador_email = NotificadorEmail(notificador_simples)
    notificador_email.enviar("Seu pedido foi enviado")

    print("\nNotificação com e-mail + SMS:")
    notificador_completo = NotificadorSMS(notificador_email)
    notificador_completo.enviar("Nova fatura disponível")
```

## Vantagens

- Adiciona funcionalidades de forma **flexível e controlada**
- Evita **herança profunda**
- Segue o princípio aberto/fechado (Open/Closed)

## Desvantagens

- Pode introduzir **muitas pequenas classes**
- A ordem dos decoradores pode afetar o comportamento

## Quando usar?

- Quando você precisa **adicionar funcionalidades específicas** a objetos sem modificar
a classe original
- Quando quer **combinar comportamentos** dinamicamente
- Quando herança seria inflexível ou causaria duplicação 

## Decorator vs Inheritance

Aspecto       | Herança                    | Decorator
------------- | -------------------------- | --------------------------------
Flexibilidade | Estática                   | Dinâmica em tempo de execução
Composição    | Não (extensão por herança) | Sim (envolvimento em camadas)
Complexidade  | Razoável                   | Pode ter muitas pequenas classes

## Referência
[Refactoring Guru – Decorator](https://refactoring.guru/pt-br/design-patterns/decorator)