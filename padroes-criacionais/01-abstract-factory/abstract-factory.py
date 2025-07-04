from abc import ABC, abstractmethod

# Produtos Abstratos
class Botao(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class Janela(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

# Produtos Concretos – Windows
class BotaoWindows(Botao):
    def render(self) -> str:
        return "Renderizando botão estilo Windows."

class JanelaWindows(Janela):
    def render(self) -> str:
        return "Renderizando janela estilo Windows."

# Produtos Concretos – Mac
class BotaoMac(Botao):
    def render(self) -> str:
        return "Renderizando botão estilo MacOS."

class JanelaMac(Janela):
    def render(self) -> str:
        return "Renderizando janela estilo MacOS."

# Fábrica Abstrata
class GUIFactory(ABC):
    @abstractmethod
    def criar_botao(self) -> Botao:
        pass

    @abstractmethod
    def criar_janela(self) -> Janela:
        pass

# Fábricas Concretas
class WindowsFactory(GUIFactory):
    def criar_botao(self) -> Botao:
        return BotaoWindows()

    def criar_janela(self) -> Janela:
        return JanelaWindows()

class MacFactory(GUIFactory):
    def criar_botao(self) -> Botao:
        return BotaoMac()

    def criar_janela(self) -> Janela:
        return JanelaMac()

# Cliente
class Aplicacao:
    def __init__(self, factory: GUIFactory):
        self.botao = factory.criar_botao()
        self.janela = factory.criar_janela()

    def renderizar_interface(self):
        print(self.botao.render())
        print(self.janela.render())

# Teste
def configurar_aplicacao(sistema: str) -> Aplicacao:
    if sistema == "Windows":
        return Aplicacao(WindowsFactory())
    elif sistema == "Mac":
        return Aplicacao(MacFactory())
    else:
        raise ValueError("Sistema não suportado.")

if __name__ == "__main__":
    app = configurar_aplicacao("Mac")
    app.renderizar_interface()
