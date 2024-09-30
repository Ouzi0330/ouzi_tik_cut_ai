import os
import urllib.request
from ouzi_tik_cut_ai import OuziTikCutAI

def update_console_code():
    # URL del archivo interactivo en GitHub
    url = "https://raw.githubusercontent.com/tu_usuario_ouzi/ouzi_tik_cut_ai/main/interactive_console.py"
    local_path = "interactive_console.py"
    
    # Descargar el archivo actualizado desde GitHub
    try:
        urllib.request.urlretrieve(url, local_path)
        print("El archivo 'interactive_console.py' se ha actualizado correctamente desde GitHub.")
    except Exception as e:
        print(f"Error al intentar actualizar el archivo: {e}")

def load_new_functions():
    # URL del archivo de nuevas funciones en GitHub
    url = "https://raw.githubusercontent.com/tu_usuario_ouzi/ouzi_tik_cut_ai/main/new_functions.py"
    local_path = "new_functions.py"
    
    try:
        urllib.request.urlretrieve(url, local_path)
        print("Se ha descargado el archivo 'new_functions.py'.")
        
        # Ejecutar las nuevas funciones descargadas
        with open(local_path) as f:
            code = compile(f.read(), local_path, 'exec')
            exec(code, globals())
        print("Se han cargado las nuevas funciones.")
    except Exception as e:
        print(f"Error al cargar nuevas funciones: {e}")

class InteractiveConsole:
    def __init__(self):
        self.ai = OuziTikCutAI()

    def start(self):
        # Actualizar el código de la consola
        update_console_code()

        print("Bienvenido a Ouzi Tik Cut AI. Escribe tus comandos o instrucciones.")
        while True:
            user_input = input(">> ")
            if user_input.startswith("cargar nuevas funciones"):
                load_new_functions()
            elif user_input.startswith("descargar video"):
                url = input("URL del video de YouTube: ")
                resolution = input("Resolución (720p, 1080p): ")
                video_path = self.ai.download_video(url, resolution)
                print(f"Video descargado: {video_path}")
            elif user_input.startswith("transcribir video"):
                video_path = input("Ruta del video: ")
                transcription = self.ai.transcribe_video(video_path)
                print(f"Transcripción: {transcription}")
            elif user_input.startswith("resumir texto"):
                text = input("Texto a resumir: ")
                summary = self.ai.summarize_text(text)
                print(f"Resumen: {summary}")
            elif user_input == "salir":
                break
            else:
                print("Comando no reconocido. Inténtalo de nuevo.")
