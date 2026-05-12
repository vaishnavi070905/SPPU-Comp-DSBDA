import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('wordnet')

text = "Natural Language Processing is a field of Artificial Intelligence that helps computers understand human language."

tokens = word_tokenize(text)
print("Tokens:", tokens)

pos_tags = nltk.pos_tag(tokens)
print("\nPOS Tags:", pos_tags)

stop_words = set(stopwords.words('english'))
filtered_words = [word for word in tokens if word.lower() not in stop_words]
print("\nAfter Stopword Removal:", filtered_words)

stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]
print("\nStemmed Words:", stemmed_words)

lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
print("\nLemmatized Words:", lemmatized_words)

documents = [
    "Natural language processing is interesting",
    "Machine learning and artificial intelligence",
    "Deep learning improves NLP models"
]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

print("\nTF-IDF Feature Names:")
print(vectorizer.get_feature_names_out())

print("\nTF-IDF Matrix:")
print(tfidf_matrix.toarray())

print("\nCompleted")

# pip install nltk scikit-learn numpy

