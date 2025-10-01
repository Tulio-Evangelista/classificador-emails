import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

# Baixar recursos do NLTK (se ainda não tiver)
nltk.download('stopwords', quiet=True)

# Inicializa o stemmer para português
stemmer = SnowballStemmer("portuguese")
stop_words = set(stopwords.words("portuguese"))

def clean_text(text):
    """
    Limpa o texto do email:
    - Remove quebras de linha e tabs
    - Remove pontuação
    - Converte para minúsculas
    """
    text = text.lower()
    text = text.replace("\n", " ").replace("\t", " ")
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    return text

def remove_stopwords(text):
    """
    Remove palavras comuns (stopwords)
    """
    words = text.split()
    filtered_words = [w for w in words if w not in stop_words]
    return " ".join(filtered_words)

def stem_text(text):
    """
    Aplica stemming: reduz palavras para sua raiz
    """
    words = text.split()
    stemmed_words = [stemmer.stem(w) for w in words]
    return " ".join(stemmed_words)

def preprocess_email(text):
    """
    Pipeline completo de pré-processamento:
    - Limpa
    - Remove stopwords
    - Aplica stemming
    """
    text = clean_text(text)
    text = remove_stopwords(text)
    text = stem_text(text)
    return text
