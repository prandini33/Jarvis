import os
import subprocess
import webbrowser
import keyboard  # Para controle de mídia
from TTS.api import TTS
import simpleaudio as sa
from database import db, CommandHistory

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

def log_command(user_id, command_id, input_type, success=True, error_message=None):
    """ Registra um comando no banco de dados """
    try:
        new_entry = CommandHistory(
            user_id=user_id,
            command_id=command_id,
            input_type=input_type,
            success=success,
            error_message=error_message
        )
        db.session.add(new_entry)
        db.session.commit()
    except Exception as e:
        print(f"Erro ao registrar comando no banco: {e}")

def execute_command(user_id, command_id, command, input_type="voz"):
    """ Processa comandos reconhecidos, executa ações e registra no banco """

    try:
        if "navegador" in command:
            speak("Abrindo o navegador.")
            webbrowser.open("https://www.google.com")

        elif "terminal" in command:
            speak("Abrindo o terminal.")
            subprocess.run(["gnome-terminal"])  # Linux (GNOME)
        
        elif "bloco de notas" in command:
            speak("Abrindo o bloco de notas.")
            subprocess.run(["gedit"])  # Linux (Gedit)

        elif "desligar" in command:
            speak("Desligando o computador em 5 segundos.")
            os.system("sleep 5 && shutdown -h now")  # Linux

        elif "reiniciar" in command:
            speak("Reiniciando o computador em 5 segundos.")
            os.system("sleep 5 && reboot")  # Linux

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

        else:
            speak("Comando não reconhecido.")
            log_command(user_id, command_id, input_type, success=False, error_message="Comando não reconhecido")
            return

        # Se o comando foi executado com sucesso, registramos no banco
        log_command(user_id, command_id, input_type, success=True)

    except Exception as e:
        speak("Houve um erro ao executar o comando.")
        log_command(user_id, command_id, input_type, success=False, error_message=str(e))
