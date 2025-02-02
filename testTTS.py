from TTS.api import TTS

# Carrega um modelo de voz em português
tts = TTS(model_name="tts_models/pt/cv/vits", progress_bar=False)

# Converte texto em áudio e salva em um arquivo
tts.tts_to_file(text="Olá, seja bem-vindo ao Jarvis!", file_path="output.wav")

print("Áudio salvo como output.wav")
