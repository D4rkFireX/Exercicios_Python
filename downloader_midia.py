#---------------------------------------------------------------------------------------
#  | Biblioteca      | Pra quê                         |
#  | --------------- | ------------------------------- |
#  | `yt_dlp`        | baixar vídeo/áudio              |
#  | `os`            | criar pastas/manipular arquivos |
#  | `pathlib`       | caminhos de arquivos            |
#
#  | `ffmpeg`        | converter áudio/vídeo    (Não é uma biblioteca e sim um programa)
#---------------------------------------------------------------------------------------

# CONVERSOR DE MÍDIA - VIDEO/AUDIO

# Dependências para este mini-sistema
#
# yt-dlp                              pip install yt-dlp
# ffmpeg                              winget install ffmpeg (Windows)

# Importação de bibliotecas
import os           # Para comandos envolvendo o sistema operacional
import yt_dlp       # Para download de vídeos e músicas
import pathlib      # Para organização de pastas

def limpa_tela():       # Função de limpar tela (Executa o comando cls caso seja Windows, senão clear para MAC/Linux)
    os.system('cls' if os.name == 'nt' else 'clear')
    
def baixar_video(url):
    # Tratando a validação de entrada do usuário ao tentar baixar o vídeo
    try:
        # Organização da pasta de donwload de vídeo
        pasta_download = pathlib.Path("videos")
        pasta_download.mkdir(exist_ok=True)
        
        # Menu de opções de qualidade        
        print(f"\n1 - 360p")
        print("2 - 480p")
        print("3 - 720p")
        print("4 - 1080p")
        print(f"5 - 1440p")
        print(f"6 - 2160p\n")
        
        # Formatos de 360p a 2160p        
        formatos = {
            1: 'bestvideo[height<=360]+bestaudio/best',
            2: 'bestvideo[height<=480]+bestaudio/best',
            3: 'bestvideo[height<=720]+bestaudio/best',
            4: 'bestvideo[height<=1080]+bestaudio/best',
            5: 'bestvideo[height<=1440]+bestaudio/best',
            6: 'bestvideo[height<=2160]+bestaudio/best',
        }
        
        # Tratando a validação de entrada do usuário ao escolher a qualidade
        try:
            qualidade = int(input("Digite o NÚMERO da qualidade desejada: "))
        except ValueError:
            print(f"\nInválido")
            return
        
        # Se a qualidade escolhida não estiver dentro dos formatos...
        if qualidade not in formatos:
            print(f"\nOpção inválida")
            return
        
        formato_escolhido = formatos[qualidade]
        
        opcoes = {
            'format': formato_escolhido,
            'outtmpl': 'videos/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
            'restrictfilenames': True,
            
            'postprocessor_args': [
                '-c:v', 'copy',
                '-c:a', 'aac'
            ],
        }
        
        print(f"\nIniciando o download...\n")
        
        # Execução da biblioteca para baixar o vídeo
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([url])
            
        print(f"\nDownload concluído")
        
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
        print(f"Ocorreu um erro ao baixar o áudio...: {erro}")

while True:
    # Introdução da aplicação
    print("=" * 50)
    print(f"Downloader de mídia -> Vídeo/Música\n")
    print(f"O que você deseja fazer?")
    print("=" * 50)
    
    # Menu
    print(f"1 - Baixar vídeo")
    print("2 - Baixar áudio")
    print("3 - Limpar tela")
    print(f"4 - Sair")
    
    try:        # Validação de entrada do usuário em um NÚMERO disponível no menu de ações
        decisao = int(input(f"Digite o NÚMERO da operação desejada: "))
    except ValueError:
        print(f"\nInválido\n")
        continue
    
    # Bloco de condições de acordo com a escolha do usuário
    if decisao == 1:
        while True:
            url = input(f"\nCole o link do vídeo ou digite 'sair': ").strip()      #.strip() remove espaços em branco no começo e final da entrada
            
            if url.lower() == "sair":
                break
            
            if not url:
                print(f"\nVocê precisa digitar um link...")
                continue
            
            baixar_video(url)
            
            while True:
                
                pergunta_download_video = input(f"\nQuer baixar mais um vídeo? ").strip()
                
                if pergunta_download_video.lower() in ["não", "nao", "n"]:
                    break
                
                elif pergunta_download_video.lower() in ["sim", "s"]:
                    break
                
                else:
                    print(f"\nDigite apenas 'sim' ou 'não'.")
                    
            if pergunta_download_video.lower() in ["não", "nao", "n"]:
                break
            
    if decisao == 2:
        while True:
            url = input("Cole o link ou digite 'sair': ").strip()
            
            if url.lower() == "sair":
                break
        
            if not url:
                print("Você precisa digitar um link válido")
                continue
            
            baixar_audio(url)
            
            while True:
                pergunta_download_audio = input(f"\nQuer baixar mais um áudio? ").strip()
                
                if pergunta_download_audio.lower() in ["não", "nao", "n"]:
                    break
                
                elif pergunta_download_audio.lower() in ["sim", "s"]:
                    break
                
                else:
                    print(f"\nDigite apenas 'sim' ou 'não'.")
                    
            if pergunta_download_audio.lower() in ["não", "nao", "n"]:
                break
    
    if decisao == 3:
        limpa_tela()
        continue
    
    if decisao == 4:
        break
    
    else:
        print(f"\nOpção inválida")