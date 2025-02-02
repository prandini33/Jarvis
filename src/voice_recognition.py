import os
import pyaudio
import speech_recognition as sr
from vosk import Model, KaldiRecognizer
from TTS.api import TTS
import simpleaudio as sa

# Caminho do modelo Vosk
MODEL_PATH = "../model/vosk-model-pt-fb-v0.1.1-20220516_2113"

# Verifica se o modelo existe
if not os.path.exists(MODEL_PATH):
    print(f"Erro: Modelo Vosk não encontrado no caminho '{MODEL_PATH}'!")
    exit(1)

# Inicializa o modelo de reconhecimento de voz Vosk
model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)

# Inicializa o microfone
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

# Inicializa o TTS Coqui
tts = TTS(model_name="tts_models/pt/cv/vits", progress_bar=False)

def speak(text):
    """ Converte texto em fala e reproduz """
    output_file = "jarvis_voice.wav"
    tts.tts_to_file(text=text, file_path=output_file)

    # Reproduz o áudio gerado
    wave_obj = sa.WaveObject.from_wave_file(output_file)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def listen():
    """ Captura áudio do microfone e retorna o texto reconhecido """
    recognizer_instance = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer_instance.adjust_for_ambient_noise(source, duration=1)  # Ajusta automaticamente para ruído do ambiente
        print("Jarvis está ouvindo...")

        try:
            audio = recognizer_instance.listen(source, timeout=5)  # Espera até 5s por fala antes de ignorar
            text = recognizer_instance.recognize_google(audio, language="pt-BR").lower()
            return text
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return ""

if __name__ == "__main__":
    speak("Olá! Estou pronto para ouvir você.")
    while True:
        print("Diga algo para o Jarvis:")
        recognized_text = listen()

        if recognized_text:
            print(f"Você disse: {recognized_text}")
            speak(f"Você disse: {recognized_text}")

            # Condição para encerrar o assistente
            if recognized_text in ["sair", "encerrar", "tchau"]:
                speak("Até logo!")
                break
        else:
            print("Nenhuma fala reconhecida.")
