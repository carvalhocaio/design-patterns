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
