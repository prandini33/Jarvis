import spacy
from text_to_speech import speak
from commands import execute_command

# Carrega o modelo NLP em português
nlp = spacy.load("pt_core_news_sm")

# Mapeamento de intenções → Permite variações de comandos
COMMAND_MAP = {
    "abrir navegador": ["abrir navegador", "navegador", "acessar internet", "abrir chrome", "abrir firefox"],
    "abrir terminal": ["abrir terminal", "iniciar terminal", "me dá um terminal", "terminal"],
    "abrir bloco de notas": ["bloco de notas", "anotação", "quero escrever algo", "abrir gedit"],
    "desligar computador": ["desligar", "desligar computador", "shutdown"],
    "reiniciar computador": ["reiniciar", "restartar", "reboot"],
    "tocar música": ["tocar música", "reproduzir música", "play"],
    "pausar música": ["pausar música", "parar música", "pause"],
    "próxima música": ["próxima música", "música seguinte", "pular faixa"],
    "música anterior": ["música anterior", "voltar música"],
    "aumentar volume": ["aumentar volume", "volume mais alto", "subir volume"],
    "diminuir volume": ["diminuir volume", "baixar volume", "volume mais baixo"],
    "sair": ["sair", "encerrar", "fechar", "até mais", "tchau"],
}

def process_command(user_input):
    """ Processa a entrada do usuário e encontra o comando correspondente """
    doc = nlp(user_input.lower())  # Processa a frase com NLP

    # Verifica se o comando corresponde a alguma intenção conhecida
    for action, variations in COMMAND_MAP.items():
        for phrase in variations:
            if phrase in user_input.lower():
                execute_command(action)
                return

    # Se não encontrar correspondência
    speak("Desculpe, não entendi esse comando.")
