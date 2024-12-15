#Bibliotheken importieren
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

#Natural Language Toolkit einbinden - punkt_tab nachtraeglich ergaenzt
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

#Datei einbinden
df = pd.read_csv("university_of_oxford_tripadvisor_reviews.csv")

#head anzeigen
print(df.head())

#Spalten auf Text pruefen
if 'text' not in df.columns:
    print("Error: No column named 'text'. Check your dataset.")
else:
    texts = df['text']

import re

def preprocess_text(text):
    # Lowercase the text
    text = text.lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    text = ' '.join([word for word in tokens if word not in stop_words])
    return text

df['cleaned_text'] = df['text'].apply(preprocess_text)

#Bag of Words
vectorizer = CountVectorizer()
bow_matrix = vectorizer.fit_transform(df['cleaned_text'])

# Lesbarkeit optimieren
bow_df = pd.DataFrame(bow_matrix.toarray(), columns=vectorizer.get_feature_names_out())
print(bow_df.head())

#Tf-idf-Maß
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(df['cleaned_text'])

# Lesbarkeit optimieren
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf_vectorizer.get_feature_names_out())
print(tfidf_df.head())

#Latente Semantische Analyse

#Singulaerwertzerlegung
n_topics = 5  # Number of topics to extract
lsa_model = TruncatedSVD(n_components=n_topics, random_state=42)
lsa_matrix = lsa_model.fit_transform(tfidf_matrix)

#Anzeige der Top Begriffe fuer jedes Thema
terms = tfidf_vectorizer.get_feature_names_out()
for i, component in enumerate(lsa_model.components_):
    top_terms = [terms[idx] for idx in component.argsort()[-10:]]  # Top 10 terms
    print(f"Topic {i+1}: {', '.join(top_terms)}")

#Optional: Matplotlib oder wordcloud zur Visualisierung nutzen.

from wordcloud import WordCloud
import matplotlib.pyplot as plt

for i, component in enumerate(lsa_model.components_):
    wordcloud = WordCloud(width=800, height=400).generate(' '.join([terms[idx] for idx in component.argsort()[-50:]]))
    plt.figure()
    plt.title(f"Topic {i+1}")
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    plt.show()