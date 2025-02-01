import threading
import keyboard  # Detecta teclas pressionadas
from voice_recognition import listen
from text_to_speech import speak
import time
from commands import execute_command
from command_processor import process_command
from web_server import run_web_server  # Importa o servidor web

def check_keyboard_exit():
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
            print(f"Você disse: {command}")
            process_command(command)
            erro_count = 0  # Reset ao reconhecer um comando válido
        else:
            erro_count += 1
            print(f"Erro {erro_count}/2: Comando não reconhecido.")
        
        if erro_count >= 2:
            print("Encerrando o Jarvis por falta de comandos reconhecidos.")
            exit(0)


if __name__ == "__main__":
    main()