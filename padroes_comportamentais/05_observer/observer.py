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
