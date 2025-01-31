from voice_recognition import listen
from text_to_speech import speak

def main():
    """ Executa o assistente Jarvis """
    speak("Olá, eu sou o Jarvis! Diga um comando.")
    
    while True:
        command = listen()
        if command:
            print("Comando reconhecido:", command)
            speak(f"Você disse: {command}")

            # Se o usuário disser "sair", encerra o assistente
            if "sair" in command.lower():
                speak("Encerrando o assistente. Até logo!")
                break

if __name__ == "__main__":
    main()
