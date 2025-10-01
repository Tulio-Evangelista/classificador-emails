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
    
 

    if request.method == "POST":
       
        email_text = request.form.get("email_text", "")

       
        email_file = request.files.get("email_file")
        if email_file:
            filename = email_file.filename.lower()
            if filename.endswith(".pdf"):
                email_text = read_pdf(email_file)
            elif filename.endswith(".txt"):
                email_text = email_file.read().decode("utf-8")
            else:
                email_text = ""  

        if email_text.strip():
            processed_text = preprocess_email(email_text)
          
            if classifier:
                pred = classifier.predict([processed_text])[0]
                category = "Produtivo" if pred == 1 else "Improdutivo"
            else:
                
                keywords = ["ajuda", "erro", "suporte", "acesso", "problema"]
                category = "Produtivo" if any(word in processed_text for word in keywords) else "Improdutivo"

           
            response = RESPONSES.get(category, "Resposta automática padrão.")
    
    return render_template("index.html", category=category, response=response, email_text=email_text)

    


if __name__ == "__main__":
    app.run(debug=True)
