# 🎙️ Voice AI Assistant (Python + GenAI)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

Projeto desenvolvido durante estudos de IA Generativa (GenAI), integrando:

## 🔄 Pipeline
🎤 Captura de áudio no navegador  
🧠 Transcrição com Whisper  
💬 Geração de resposta com LLM (OpenAI)  
🔊 Conversão de texto em voz (TTS)  
🧠 Como funciona  

## O fluxo do projeto:

Áudio (microfone) > Transcrição (Whisper) > Entrada para IA (LLM) > Resposta em texto > Conversão para áudio (gTTS) 

## 🛠️ Tecnologias utilizadas
Python  
Google Colab / Jupyter  
JavaScript (MediaRecorder API) → captura de áudio  
Whisper → reconhecimento de fala (Speech-to-Text)  
OpenAI API → geração de resposta com IA  
gTTS (Google Text-to-Speech) → síntese de voz  

## 📦 Instalação

Clone o repositório:

git clone https://github.com/seu-usuario/voice-ai-assistant.git  
cd voice-ai-assistant

Instale as dependências:  

pip install -r requirements.txt  

## 🔑 Configuração
 
Defina sua API Key da OpenAI:  
export OPENAI_API_KEY="sua-chave-aqui"  
Ou no Python:  
import os  
os.environ["OPENAI_API_KEY"] = "sua-chave"  

## ▶️ Execução
python app.py

## ⚠️ Observação:
A captura de áudio funciona melhor no Google Colab, pois depende do navegador.

## 📌 Funcionalidades
🎙️ Gravação de áudio via navegador  
🧠 Transcrição automática  
💬 Interação com modelo de linguagem  
🔊 Resposta em áudio  
🚧 Melhorias futuras  
Interface web com Streamlit  
Integração com APIs de voz em tempo real  
Uso de modelos locais (offline)  
Deploy em nuvem  

## 📊 Aplicações
Assistentes virtuais  
Chatbots com voz  
Automação de atendimento  
Ferramentas de acessibilidade  

## 👨‍💻 Autor
Guilherme Ruiz  
Projeto desenvolvido para fins educacionais durante estudos em IA Generativa.
