# Email Classifier - Case Técnico

## Descrição
Aplicação web simples que classifica emails em **Produtivo** ou **Improdutivo** e sugere respostas automáticas.

Funcionalidades:
- Upload de emails em **texto ou PDF**
- Pré-processamento de texto
- Classificação automática
- Resposta automática (fixa ou via OpenAI GPT)

## Estrutura do Projeto
- `app.py` → aplicação Flask
- `utils.py` → funções de pré-processamento e resposta
- `model_train.py` → script para treinar modelo
- `templates/index.html` → interface web
- `static/styles.css` → estilos
- `requirements.txt` → dependências Python
- `dados_exemplo/` → emails de teste

## Como Rodar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/email-classifier.git
cd email-classifier/email-ai

2- Crie e ative o ambiente virtual:
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

3- Instale as dependências:
pip install -r requirements.txt

4-Treine o modelo (ou use o já treinado):
python model_train.py

5-Execute a aplicação:
python app.py

6-Acesse no navegador:
http://127.0.0.1:5000


