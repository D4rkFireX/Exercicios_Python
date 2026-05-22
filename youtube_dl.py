#  | Biblioteca      | Pra quê                         |
#  | --------------- | ------------------------------- |
#  | `yt_dlp`        | baixar vídeo/áudio              |
#  | `ffmpeg`        | converter áudio/vídeo           |
#  | `os`            | criar pastas/manipular arquivos |
#  | `pathlib`       | caminhos de arquivos            |

# CONVERSOR DE MÍDIA DO YOUTUBE - VIDEO/AUDIO
# Dependências -> yt-dlp              pip install yt-dlp

# Importação da Biblioteca
import yt_dlp

def baixar_video(url):
    try:
        print("Iniciando o download...")
        with yt_dlp.YoutubeDL() as ydl:
            ydl.download([url])
        print("Download concluído!")
    except Exception as erro:
        print(f"Ocorreu um erro ao baixar o vídeo: {erro}")
    
print(f"Downloader de mídia do Youtube -> Vídeo/Música\n")
while True:
    print("1 - Vídeo")
    print("2 - Música")
    print(f"3 - Sair\n")
    
    try:
        decisao = int(input(f"Digite o NÚMERO da operação desejada: \n"))
    except ValueError:
        print("Inválido")
        continue
        
    if decisao == 1:
        url = input("Cole o link ou digite 'sair': ").strip()
        if url.lower() in ["sair"]:
            break
        
        if not url:
            print("Você precisa digitar um link")
            continue
        
        baixar_video(url)
            
    elif decisao == 2:
        print("Função em Desenvolvimento...")
    
    elif decisao == 3:
        print("Encerrando a Aplicação")
        break