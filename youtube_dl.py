#  | Biblioteca      | Pra quê                         |
#  | --------------- | ------------------------------- |
#  | `yt_dlp`        | baixar vídeo/áudio              |
#  | `os`            | criar pastas/manipular arquivos |
#  | `pathlib`       | caminhos de arquivos            |
#  | `ffmpeg`        | converter áudio/vídeo    (Não inclusa neste exercício)

# CONVERSOR DE MÍDIA DO YOUTUBE - VIDEO/AUDIO
# Dependências -> yt-dlp              pip install yt-dlp

# Importação da Biblioteca
import os
import yt_dlp
import pathlib

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def baixar_video(url):
    try:
        pasta_download = pathlib.Path("videos")
        pasta_download.mkdir(exist_ok=True)
        
        print("1 - 360p")
        print("2 - 480p")
        print("3 - 720p")
        print(f"4 - 1080p\n")
        
        formatos = {
            1: 'best[height<=360]',
            2: 'best[height<=480]',
            3: 'best[height<=720]',
            4: 'best[height<=1080]'
        }
        
        try:
            qualidade = int(input("Digite o NÚMERO da qualidade desejada: "))
        except ValueError:
            print("Inválido")  
            return      
        
        if qualidade not in formatos:
            print("Opção inválida")
            return
        
        formato_escolhido = formatos[qualidade]
        
        opcoes = {
            'format': formato_escolhido,
            'outtmpl': 'videos/%(title)s.%(ext)s'
        }     
           
        print(f"\nIniciando o download...\n")
        
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([url])
            
        print("Download concluído!")
        
    except Exception as erro:
        print(f"Ocorreu um erro ao baixar o vídeo...: {erro}")

def baixar_audio(url):
    try:
        pasta_download = pathlib.Path("audios")
        pasta_download.mkdir(exist_ok=True)
                
        opcoes = {
            'format': 'bestaudio',
            'outtmpl': 'audios/%(title)s.%(ext)s'
        }
                
        print(f"\nIniciando o download...\n")

        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([url])

        print("Download concluído!")
                
    except Exception as erro:
        print(f"Ocorreu ao baixar um áudio...: {erro}")

print("=" * 50)
print(f"Downloader de mídia do Youtube -> Vídeo/Música\n")
print("=" * 50)

while True:
    print("1 - Vídeo")
    print("2 - Música")
    print("3 - Limpar Tela")
    print(f"4 - Sair\n")

    try:
        decisao = int(input(f"Digite o NÚMERO da operação desejada: "))
    except ValueError:
        print("Inválido")
        continue

    if decisao == 1:
        while True:
            url = input("Cole o link ou digite 'sair': ").strip()
            if url.lower() == "sair":
                break

            if not url:
                print("Você precisa digitar um link")
                continue

            baixar_video(url)
            
            pergunta_download_video = input("Quer baixar mais um vídeo? ").strip()
            if pergunta_download_video.lower() in ["sim", "s"]:
                continue
            elif pergunta_download_video.lower() in ["não", "nao", "n"]:
                break

    elif decisao == 2:
        while True:
            url = input("Cole o link ou digite 'sair': ").strip()
            if url.lower() == "sair":
                break
        
            if not url:
                print("Você precisa digitar um link válido")
                continue
            
            baixar_audio(url)
            
            pergunta_download_audio = input("Quer baixar mais um áudio? ").strip()
            if pergunta_download_audio.lower() in ["sim", "s"]:
                continue
            elif pergunta_download_audio.lower() in ["não", "nao", "n"]:
                break

    elif decisao == 3:
        limpa_tela()

    elif decisao == 4:
        print("Encerrando a Aplicação")
        break
