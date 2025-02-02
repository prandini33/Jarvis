# 🔊 OX - Assistente Pessoal Inteligente

**OX** é um assistente pessoal controlado por voz que executa comandos no seu computador, como abrir programas, controlar mídia e responder a comandos via interface web.

## 🚀 Funcionalidades
- 🔍 **Reconhecimento de voz** (offline com Vosk)
- 🎤 **Síntese de voz** (pyttsx3)
- 🖥️ **Controle do sistema** (abrir programas, desligar PC)
- 🎵 **Comandos de mídia** (tocar/pausar música, ajustar volume)
- 🌐 **Interface web** para controle remoto via navegador

## 📌 Instalação

### **1️⃣ Clonar o repositório**
```bash
git clone https://github.com/prandini33/ox.git
cd ox
```

### **2️⃣ Criar ambiente virtual**
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### **3️⃣ Instalar dependências**
```bash
pip install -r requirements.txt
```

### **4️⃣ Baixar o modelo Vosk**
1. Acesse: [https://alphacephei.com/vosk/models](https://alphacephei.com/vosk/models)
2. Baixe **vosk-model-small-pt**
3. Extraia a pasta para `ox/model/`

---

## ▶️ Como Usar
### **Executar o Ox**
```bash
python3 src/main.py
```

### **Comandos Disponíveis**
| Comando               | Ação |
|-----------------------|--------------------------------|
| "Abrir navegador"    | Abre o Chrome/Firefox |
| "Abrir terminal"     | Abre o terminal do sistema |
| "Tocar música"       | Inicia a reprodução de áudio |
| "Aumentar volume"    | Aumenta o volume do sistema |
| "Diminuir volume"    | Abaixa o volume do sistema |
| "Sair"               | Fecha o assistente |

### **Encerrar o Ox**
- **Pressione `ESC`** no teclado.
- **Ou diga "Sair"** duas vezes para ele se fechar automaticamente.

---

## 🌐 Interface Web
O Ox pode ser controlado pelo navegador:
```bash
http://localhost:5000
```
- Botões para enviar comandos remotamente.
- Permite pausar música, abrir aplicativos, etc.

---

## 🤝 Contribuindo
Quer contribuir? Siga estes passos:
1. **Fork** o projeto
2. **Crie uma branch** (`git checkout -b minha-feature`)
3. **Faça um commit** (`git commit -m "feat: minha nova funcionalidade"`)
4. **Envie um Pull Request**

---

## 📜 Licença
Este projeto está licenciado sob a **MIT License**.

---

### 📌 **Autor**
🔗 GitHub: [prandini33](https://github.com/prandini33)  
✉️ Email: lzprandini@gmail.com

