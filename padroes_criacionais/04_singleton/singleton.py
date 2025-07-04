class Singleton:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            print("Criando nova instância")
        return cls._instancia

    def __init__(self):
        self.valor = None

# Teste
if __name__ == "__main__":
    s1 = Singleton()
    s1.valor = "Config A"

    s2 = Singleton()
    print(s2.valor)  # Config A

    print(f"s1 é s2? {s1 is s2}")  # True
