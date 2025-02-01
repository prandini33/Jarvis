import threading
import keyboard  # Detecta teclas pressionadas
from voice_recognition import listen
from text_to_speech import speak
import time
from commands import execute_command
from command_processor import process_command

def check_keyboard_exit():
    keyboard.wait("esc")  # Espera até que ESC seja pressionado
    speak("Encerrando o assistente. Até logo!")
    exit(0)


def main():
    """ Executa o assistente Jarvis """
    speak("Olá, eu sou o Jarvis! Pressione ESC para me encerrar.")

    # Inicia um thread para monitorar o teclado
    threading.Thread(target=check_keyboard_exit, daemon=True).start()

    while True:
        command = listen()
        if command:
            print("Comando reconhecido:", command)
            speak(f"Você disse: {command}")
            
            # Processa o comando reconhecido com NLP
            process_command(command)

if __name__ == "__main__":
    main()