import threading
import keyboard  # Detecta teclas pressionadas
import time
import os
import simpleaudio as sa
from TTS.api import TTS
from commands import execute_command
from command_processor import process_command
from web_server import run_web_server  # Importa o servidor web
import pyaudio
import speech_recognition as sr
from vosk import Model, KaldiRecognizer

# Configuração do modelo Vosk
MODEL_PATH = "../model/vosk-model-pt-fb-v0.1.1-20220516_2113"

# Verifica se o modelo existe
if not os.path.exists(MODEL_PATH):
    print(f"Erro: Modelo Vosk não encontrado no caminho '{MODEL_PATH}'!")
    exit(1)

# Inicializa reconhecimento de voz
model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

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

def listen():
    """ Captura áudio do microfone e retorna o texto reconhecido """
    recognizer_instance = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer_instance.adjust_for_ambient_noise(source, duration=1)
        print("Jarvis está ouvindo...")

        try:
            audio = recognizer_instance.listen(source, timeout=5)
            text = recognizer_instance.recognize_google(audio, language="pt-BR").lower()
            return text
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return ""

def check_keyboard_exit():
    """ Monitora a tecla ESC para encerrar o assistente """
    keyboard.wait("esc")  # Espera até que ESC seja pressionado
    speak("Encerrando o assistente. Até logo!")
    exit(0)

def main():
    """ Executa o assistente Jarvis """
    speak("Olá, eu sou o Jarvis! Pressione ESC para me encerrar.")

    # Inicia um thread para monitorar o teclado
    threading.Thread(target=check_keyboard_exit, daemon=True).start()

    erro_count = 0  # Contador de comandos não reconhecidos

    while True:
        command = listen()
        if command:
            print("Comando reconhecido:", command)
            process_command(command)
            erro_count = 0  # Reset ao reconhecer um comando válido
        else:
            erro_count += 1
            print(f"Erro {erro_count}/2: Comando não reconhecido.")
        
        if erro_count >= 2:
            print("Encerrando o Jarvis por falta de comandos reconhecidos.")
            speak("Não reconheci dois comandos seguidos. Encerrando o sistema.")
            exit(0)

if __name__ == "__main__":
    main()
