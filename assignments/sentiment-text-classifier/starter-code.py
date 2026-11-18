from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

texts = [
    "I love this game",
    "This movie is wonderful",
    "The food tastes great",
    "I am happy with my new book",
    "That was a fun day",
    "The music sounds beautiful",
    "I hate waiting in line",
    "This movie is boring",
    "The food tastes awful",
    "I am unhappy with this book",
    "That was a terrible day",
    "The music sounds annoying",
]

labels = [
    "positive",
    "positive",
    "positive",
    "positive",
    "positive",
    "positive",
    "negative",
    "negative",
    "negative",
    "negative",
    "negative",
    "negative",
]

# 1. Separe as frases e os rótulos em dados de treino e de teste.
# X_train, X_test, y_train, y_test = ...

# 2. Transforme as frases em contagens de palavras.
# vectorizer = CountVectorizer()
# X_train_counts = ...
# X_test_counts = ...

# 3. Treine o modelo e mostre sua acuracia nos dados de teste.
# model = MultinomialNB()
# ...

# 4. Peca uma frase ao usuario e mostre o sentimento previsto.
# new_text = input("Digite uma frase em ingles: ")
# new_text_counts = ...
# prediction = ...
# print("Sentimento previsto:", prediction)
