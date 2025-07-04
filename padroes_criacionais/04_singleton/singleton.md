# Padrão de Projeto: Singleton

O padrão **Singleton** garante que **uma classe tenha apenas uma instância** e fornece um
ponto global de acesso a ela.

Idel para recursos que **devem ser únicos** no sistema, como um gerenciador de
configuração, log, conexão com banco, etc.

## Intenção

Evitar múltiplas instâncias de uma classe e garantir acesso **controlado** e **compartilhado**
à única instância existente.

## Estrutura

### Participantes

- **Singleton (Instância única)**: armazena a própria instância e fornece o ponto de
acesso (`get_instance()` ou similar).
- **Client (Cliente)**: usa o ponto de acesso e trabalha com a única instância.

## Exemplo em Python

Python oferece várias formas de implementar Singleton. Aqui está uma versão clássica com
**controle via** `__new__`:

```py
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
```

## Vantagens

- Garante existência de uma única instância
- Fornece ponto global de acesso
- Pode ser usado para recursos globais e compartilhados

## Desvantagens

- **Anti-padrão** em alguns contextos (acoplamento global, dificuldade de testar)
- Pode violar o princípio da responsabilidade única
- Pode causar problemas em ambientes multithread sem controle adequado

## Versão Thread-Safe (com `threading.Lock`)

```py
import threading

class SingletonThreadSafe:
    _instancia = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instancia is None:
                cls._instancia = super().__new__(cls)
                print("Instância segura criada")
        return cls._instancia
```

## Quando usar?

- Quando for **essencial** ter uma única instância compartilhada no sistema
- Quando quiser controle centralizado de um recurso
- Evite se puder usar **injeção de dependẽncia** ou **fábricas**

## Referência
[Refactoring Guru - Singleton](https://refactoring.guru/pt-br/design-patterns/singleton)