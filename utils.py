import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import PyPDF2
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


nltk.download('stopwords', quiet=True)


stemmer = SnowballStemmer("portuguese")
stop_words = set(stopwords.words("portuguese"))


def read_pdf(file):
    text = ""
    reader = PyPDF2.PdfReader(file)
    for page in reader.pages:
        text += page.extract_text() + " "
    return text.strip()

    
def generate_response(email_text, category):
    if category == "Produtivo":
        system_prompt = "Você é um assistente profissional que responde emails de trabalho."
        user_prompt = f"Responda profissionalmente este email: {email_text}"
    else:
        system_prompt = "Você é um assistente cordial que responde emails brevemente."
        user_prompt = f"Responda de forma cordial e breve este email: {email_text}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.5,
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Erro ao gerar resposta: {e}"

def clean_text(text):
    text = text.lower()
    text = text.replace("\n", " ").replace("\t", " ")
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    return text

def remove_stopwords(text):
    words = text.split()
    filtered_words = [w for w in words if w not in stop_words]
    return " ".join(filtered_words)

def stem_text(text):
    words = text.split()
    stemmed_words = [stemmer.stem(w) for w in words]
    return " ".join(stemmed_words)

def preprocess_email(text):
    text = text.lower()
    return text

def classify_email(text):
    """
    Classifica um email como Produtivo ou Improdutivo
    baseado em palavras-chave simples.
    """
    keywords_produtivo = [
        "ajuda", "suporte", "acesso", "sistema",
        "cadastro", "erro", "problema", "senha",
        "login", "falha", "chamado", "conta",
        "pagamento", "fatura", "boleto"
    ]

    text_lower = text.lower()
    if any(word in text_lower for word in keywords_produtivo):
        return "Produtivo"
    return "Improdutivo"