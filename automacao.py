import os
import shutil

PASTA_ALVO = "arquivo.teste"

CATEGORIAS = {
    "Imagens": [".png", ".jpg", ".jpeg", ".gif"],
    "Documentos_PDF": [".pdf"],
    "Musicas": [".mp3", ".wav"],
    "Planilhas": [".xlsx", ".csv"],
    "Textos": [".txt"]
}

print(f"--- Iniciando automação na pasta '{PASTA_ALVO}' ---")


if os.path.exists(PASTA_ALVO):
    for arquivo in os.listdir(PASTA_ALVO):
        
      
        if arquivo.endswith(".py"):
            continue

       
        caminho_original = os.path.join(PASTA_ALVO, arquivo)

        
        if os.path.isfile(caminho_original):
            nome, extensao = os.path.splitext(arquivo)
            extensao = extensao.lower()

           
            for pasta, extensoes in CATEGORIAS.items():
                if extensao in extensoes:
                    
                    pasta_destino = os.path.join(PASTA_ALVO, pasta)
                    os.makedirs(pasta_destino, exist_ok=True)

              
                    caminho_destino = os.path.join(pasta_destino, arquivo)

                   
                    shutil.move(caminho_original, caminho_destino)
                    print(f"Movido: {arquivo} --> {pasta_destino}")
                    break

    print("--- Organização concluída! ---")
else:
    print(f"A pasta '{PASTA_ALVO}' não existe no diretório atual.")