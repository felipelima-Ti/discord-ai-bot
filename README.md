# 🤖 Discord AI Agent

Um bot de Discord inteligente conectado a um agente de IA local, capaz de responder usuários em tempo real utilizando modelos open-source (via Ollama). Totalmente gratuito.

---

##  Funcionalidades

*  Responde mensagens de usuários no Discord
*  Inteligência artificial local (sem custos de API)
*  Memória de conversa
*  Respostas rápidas via API local
*  Funciona offline (após baixar voce baixar o modelo)

---

##  Arquitetura

```
Discord → Bot (Python) → API (FastAPI) → IA Local (Ollama)
```

---

## 📁 Estrutura do Projeto

```
agent/
├── agent.py          # API do agente (FastAPI)
├── bot.py            # Bot do Discord
├── requirements.txt  # Dependências
├── .env              # Variáveis de ambiente (NÃO subir)
└── .gitignore        # Arquivos ignorados
```

---

## ⚙️ Tecnologias Utilizadas

* Python
* FastAPI
* discord.py
* Ollama (IA local)

---

##  Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/discord-ai-bot.git
cd discord-ai-bot
```

---

### 2. Crie um ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

##  Configuração

### 1. Crie o arquivo `.env`

```env
DISCORD_TOKEN=seu_token_aqui
```

---

### 2. Configure o bot

No arquivo `bot.py`, configure a url padrao:

```python
API_URL = "http://127.0.0.1:8000/chat"
```

---

##  Rodando a IA local

Instale o Ollama e execute:

```bash
ollama run llama3
```

---

## ▶ Executando o projeto

### 1. Inicie o agente

```bash
uvicorn agent:app --host 0.0.0.0 --port 8000
```

---

### 2. Inicie o bot

```bash
python bot.py
```

---

##  Como usar

No Discord:

```
!ai Olá, tudo bem?
```

O bot responderá utilizando IA local.

---

## 🔐 Segurança

* Nunca compartilhe seu `DISCORD_TOKEN`
* Use `.env` para variáveis sensíveis
* `.gitignore` protege seus dados

---

##  Melhorias futuras

*  Deploy online 24h
*  Respostas em streaming


---

##  Licença

Este projeto é open-source e pode ser utilizado livremente para fins educacionais e comerciais.

---

##  Autor

Desenvolvido por mim 
Sinta-se livre para me ajudar!

---
