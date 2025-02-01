import os
import subprocess
import webbrowser
from text_to_speech import speak

def execute_command(command):
    """ Processa comandos reconhecidos e executa ações """
    
    if "navegador" in command:
        speak("Abrindo o navegador.")
        webbrowser.open("https://www.google.com")

    elif "terminal" in command:
        speak("Abrindo o terminal.")
        subprocess.run(["gnome-terminal"])  # Linux (GNOME)
        # subprocess.run(["x-terminal-emulator"])  # Alternativa para outras distros

    elif "bloco de notas" in command:
        speak("Abrindo o bloco de notas.")
        subprocess.run(["gedit"])  # Linux (Gedit)
        # subprocess.run(["notepad.exe"])  # Windows

    elif "desligar" in command:
        speak("Desligando o computador.")
        os.system("shutdown -h now")  # Linux
        # os.system("shutdown /s /t 0")  # Windows

    elif "reinicia"r in command:
        speak("Reiniciando o computador.")
        os.system("reboot")  # Linux
        # os.system("shutdown /r /t 0")  # Windows

     elif "tocar música" in command:
        speak("Tocando música.")
        subprocess.run(["xdg-open", "/caminho/para/sua/música.mp3"])  # Ajuste o caminho para um arquivo local

    elif "pausar música" in command:
        speak("Pausando música.")
        keyboard.press_and_release("play/pause media")  # Emula tecla de mídia

    elif "próxima música" in command:
        speak("Pulando para a próxima música.")
        keyboard.press_and_release("next track media")

    elif "música anterior" in command:
        speak("Voltando para a música anterior.")
        keyboard.press_and_release("previous track media")

    elif "aumentar volume" in command:
        speak("Aumentando o volume.")
        keyboard.press_and_release("volume up")

    elif "diminuir volume" in command:
        speak("Diminuindo o volume.")
        keyboard.press_and_release("volume down")
        

    elif "sair" in command:
        speak("Encerrando o assistente. Até logo!")
        exit(0)

    else:
        speak("Desculpe, não entendi o comando.")
