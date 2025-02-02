import os
import subprocess
import webbrowser
import keyboard  # Para controle de mídia
from TTS.api import TTS
import simpleaudio as sa

# Inicializa Coqui TTS
tts = TTS(model_name="tts_models/pt/cv/vits", progress_bar=False)

def speak(text):
    """ Converte texto em fala e reproduz """
    output_file = "jarvis_voice.wav"
    tts.tts_to_file(text=text, file_path=output_file)

    # Reproduz áudio gerado
    wave_obj = sa.WaveObject.from_wave_file(output_file)
    play_obj = wave_obj.play()
    play_obj.wait_done()

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
        speak("Desligando o computador em 5 segundos.")
        os.system("sleep 5 && shutdown -h now")  # Linux
        # os.system("shutdown /s /t 5")  # Windows

    elif "reiniciar" in command:
        speak("Reiniciando o computador em 5 segundos.")
        os.system("sleep 5 && reboot")  # Linux
        # os.system("shutdown /r /t 5")  # Windows

    elif "tocar música" in command:
        speak("Tocando música.")
        keyboard.press_and_release("play/pause media")

    elif "pausar música" in command:
        speak("Pausando música.")
        keyboard.press_and_release("play/pause media")

    elif "próxima música" in command:
        speak("Pulando para a próxima música.")
        keyboard.press_and_release("next track media")

    elif "música anterior" in command:
        speak("Voltando para a música anterior.")
        keyboard.press_and_release("previous track media")

   
