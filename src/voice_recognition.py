import os
import pyaudio
from vosk import Model, KaldiRecognizer

# Caminho para o modelo dentro da pasta "model"
MODEL_PATH = "../model/vosk-model-pt-fb-v0.1.1-20220516_2113"

# Verifica se o modelo existe
if not os.path.exists(MODEL_PATH):
    print(f"Erro: Modelo Vosk não encontrado no caminho '{MODEL_PATH}'!")
    print("Certifique-se de que o modelo está corretamente extraído dentro da pasta 'model'.")
    exit(1)

# Inicializa o modelo Vosk
model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)

# Configuração do microfone
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, frames_per_buffer=8192, input=True)
stream.start_stream()

def listen():
    """ Captura áudio do microfone e retorna o texto reconhecido """
    print("Fale algo...")
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            return result  # Retorna o texto reconhecido

if __name__ == "__main__":
    recognized_text = listen()
    print("Você disse:", recognized_text)
