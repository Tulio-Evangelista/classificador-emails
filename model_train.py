from utils import preprocess_email
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib


emails = [
    # Produtivos
    "Preciso de ajuda com meu cadastro, não consigo acessar o sistema.",
    "Meu boleto não foi gerado corretamente, preciso de suporte.",
    "Favor atualizar o status da requisição #123.",
    "Não consigo fazer login na minha conta, podem ajudar?",
    "O pagamento da minha fatura deu erro no sistema.",
    "Gostaria de abrir um chamado técnico para corrigir uma falha.",
    "Solicito informações sobre meu contrato de serviço.",
    "Estou com problema no aplicativo, não abre a tela de login.",
    "O relatório financeiro não está disponível no sistema.",
    "Meu cartão foi bloqueado, preciso desbloquear urgentemente.",

    # Improdutivos
    "Parabéns pelo seu excelente trabalho!",
    "Feliz Natal e boas festas a todos!",
    "Obrigado pelo retorno da última reunião.",
    "Desejo um ótimo fim de semana para toda a equipe.",
    "Gostaria de marcar um café para conversarmos.",
    "Bom dia! Apenas passando para cumprimentar.",
    "Foi ótimo o happy hour de ontem!",
    "Estou organizando um almoço de confraternização.",
    "Desejo um feliz aniversário para você.",
    "Boa tarde, apenas passando para agradecer."
]

labels = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]




emails_preprocessed = [preprocess_email(email) for email in emails]


pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', MultinomialNB())
])


X_train, X_test, y_train, y_test = train_test_split(
    emails_preprocessed, labels, test_size=0.3, random_state=42, stratify=labels
)


y_pred = pipeline.predict(X_test)
print("Acurácia:", accuracy_score(y_test, y_pred))
print("Relatório de classificação:\n", classification_report(y_test, y_pred))


joblib.dump(pipeline, 'email_classifier.joblib')
print("Modelo salvo em 'email_classifier.joblib'")

for e in emails:
    print(f"{e} => {pipeline.predict([preprocess_email(e)])[0]}")