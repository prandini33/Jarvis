import pyttsx3

# Inicializa o motor de voz
engine = pyttsx3.init()

# Ajusta as configurações de fala
engine.setProperty('rate', 110)  # Reduz a velocidade da fala (padrão: 200)
engine.setProperty('volume', 1.0)  # Volume máximo (1.0)
voices = engine.getProperty('voices')

# Tenta selecionar uma voz masculina/feminina mais natural (ajuste conforme necessário)
for voice in voices:
    if "brazil" in voice.name.lower():  # Para Português do Brasil
        engine.setProperty('voice', voice.id)
        break

def speak(text):
    """ Faz o Jarvis falar de maneira clara """
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Olá, estou funcionando corretamente e agora minha voz está melhor!")
