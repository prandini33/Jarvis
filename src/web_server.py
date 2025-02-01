from flask import Flask, render_template, request, jsonify
from command_processor import process_command
import threading

app = Flask(__name__)

@app.route("/")
def home():
    """ Renderiza a interface web """
    return render_template("index.html")

@app.route("/send_command", methods=["POST"])
def send_command():
    """ Recebe comandos da interface web e os processa """
    data = request.get_json()
    command = data.get("command", "").lower()
    
    if command:
        process_command(command)
        return jsonify({"status": "success", "message": f"Comando '{command}' enviado."})
    else:
        return jsonify({"status": "error", "message": "Comando inválido."}), 400

def run_web_server():
    """ Inicia o servidor Flask em uma thread separada """
    app.run(host="0.0.0.0", port=5000, debug=True)

if __name__ == "__main__":
    threading.Thread(target=run_web_server, daemon=True).start()
