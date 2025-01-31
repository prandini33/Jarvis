import pyttsx3

# Inicializa o motor de voz
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Ajusta a velocidade da fala

def speak(text):
    """ Faz o Jarvis falar o texto fornecido """
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Olá, estou funcionando corretamente!")
