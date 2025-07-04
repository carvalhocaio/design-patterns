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
