# Padrão de Projeto: Proxy

O padrão **Proxy** fornece um **substituto ou representante** de outro objeto para
**controlar o acesso** a ele. O proxy age como um intermediário entre o cliente e o objeto real.

Ideal quando você precisa **adiar, controlar, proteger ou monitorar** o acesso a um objeto real.

## Intenção

Fornecer um objeto intermediário que tem a **mesma interface** do objeto real, mas pode
adicionar lógica como:

- Controle de acesso
- Cache
- Log
- Contagem de chamadas
- Lazy initialization
- Acesso remoto

## Estrutura

### Participantes:

- **Subject (Sujeito)**: interface comum entre o objeto real e o proxy.
- **RealSubject**: objeto real que faz o trabalho.
- **Proxy**: controla o acesso ao `RealSubject`, implementa a mesma interface.

## Exemplo em Python

Vamos modelar um **serviço de vídeo** (como um YouTube), mas adicionar um proxy que
**faz cache** de vídeos assistidos para evitar chamadas repeditas.

```py
from abc import ABC, abstractmethod
import time

# Interface comum
class ServicoVideo(ABC):
    @abstractmethod
    def assistir(self, video_id: str): pass

# Objeto real
class Youtube(ServicoVideo):
    def assistir(self, video_id: str):
        print(f"🔴 Carregando vídeo {video_id} do YouTube...")
        time.sleep(1)  # simula tempo de rede
        print(f"▶️ Reproduzindo {video_id}")

# Proxy com cache
class YoutubeProxy(ServicoVideo):
    def __init__(self):
        self._youtube = Youtube()
        self._cache = {}

    def assistir(self, video_id: str):
        if video_id in self._cache:
            print(f"✅ Vídeo {video_id} recuperado do cache.")
            print(f"▶️ Reproduzindo {video_id}")
        else:
            self._youtube.assistir(video_id)
            self._cache[video_id] = True

# Cliente
def assistir_video(servico: ServicoVideo, video_id: str):
    servico.assistir(video_id)

# Teste
if __name__ == "__main__":
    youtube = YoutubeProxy()
    assistir_video(youtube, "Aula-01")
    print("\n---\n")
    assistir_video(youtube, "Aula-02")
    print("\n---\n")
    assistir_video(youtube, "Aula-01")  # este virá do cache
```

## Vantagens

- Adiciona **comportamento extra** sem alterar o objeto real
- Útil para **controle de acesso, cache, logging, lazy loading**
- Reduz o custo de objetos pesados ou remotos

## Desvantagens

- Adiciona complexidade e indireção
- Precisa manter interface consistente com o objeto real

## Quando usar?

- Quando quer controlar o acesso a um objeto **caro, sensível ou remoto**
- Quando precisa de **cache** ou **log** sem modificar o objeto original
- Quando deseja **carregamento sob demanda (lazy loading)**

## Proxy vs Decorator vs Facade

Padrão    | Objetivo                  | Envolve o objeto real?
--------- | ------------------------- | ----------------------
Proxy     | Controle de acesso        | Sim
Decorator | Adicionar funcionalidades | Sim
Facade    | Interface simplificada    | Não necessariamente

## Referência
[Refactoring Guru – Proxy](https://refactoring.guru/pt-br/design-patterns/proxy)