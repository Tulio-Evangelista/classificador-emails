from flask import Flask, render_template, request
from utils import preprocess_email, read_pdf, generate_response
import os
from dotenv import load_dotenv
from joblib import load
import openai
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import preprocess_email, read_pdf, generate_response


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
app = Flask(__name__)



try:
    classifier = load("email_classifier.joblib")
except:
    classifier = None  


RESPONSES = {
    "Produtivo": "Olá! Recebemos sua solicitação e vamos processá-la em breve.",
    "Improdutivo": "Obrigado pelo seu contato! Sua mensagem foi recebida."
}

@app.route("/", methods=["GET", "POST"])
def index():
    category = None
    response = None
    email_text = ""
    
 

     try:
    print(" templates path:", app.template_folder)
    print(" arquivos na raiz:", os.listdir(".")
        return render_template("index.html", category=category, response=response, email_text=email_text)
    except Exception as e:
        app.logger.error(f"Erro ao renderizar template: {e}")
        return f"Erro interno: {e}", 500

  
