import os
import pyaudio
import speech_recognition as sr
from vosk import Model, KaldiRecognizer

# Caminho correto para o modelo dentro da pasta "model"
MODEL_PATH = "../model/vosk-model-pt-fb-v0.1.1-20220516_2113"

# Verifica se o modelo existe
if not os.path.exists(MODEL_PATH):
    print(f"Erro: Modelo Vosk não encontrado no caminho '{MODEL_PATH}'!")
    exit(1)

# Inicializa o modelo Vosk
model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)

# Inicializa o microfone com ajustes para reduzir falsos positivos
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

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
    print("Teste de reconhecimento de voz. Fale algo...")
    recognized_text = listen()
    print("Você disse:", recognized_text)
