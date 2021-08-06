import contractions
import re
from bs4 import BeautifulSoup
import nltk
from nltk import word_tokenize
from textblob import TextBlob
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
import string
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import unidecode
import pickle

###Preprocess Test Data
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


wordnet_map = {"N":wordnet.NOUN, "V":wordnet.VERB, "J":wordnet.ADJ, "R":wordnet.ADV}
def lemmatize_words(text):
    pos_tagged_text = nltk.pos_tag(text.split())
    return " ".join([lemmatizer.lemmatize(word, wordnet_map.get(pos[0], wordnet.NOUN)) for word, pos in pos_tagged_text])


def nlp_tokenizer(text):
    word_tokens = word_tokenize(text)
    return word_tokens

def basic_cleaning(text):
    text=text.lower()
    word_tokens=nlp_tokenizer(text)
    text = [x for x in word_tokens if
            (x not in stop_words and x not in string.punctuation and not x.isdigit())]
    text = ' '.join(text)
    text= text.strip()
    return text


def preprocessing(text):
    text = BeautifulSoup(text, 'html5lib').get_text()
    text = re.sub(r'https?:\/\/.*[\r\n]*', '', text)
    text=contractions.fix(text)
    text = unidecode.unidecode(text)
    b = TextBlob(text)
    text=basic_cleaning(str(b))
    text = re.sub('\W+',' ', text )
    text=lemmatize_words(text)
    return text

### Load data
tf1 = pickle.load(open("Models/feature.pkl", 'rb'))
model=pickle.load(open("Models/naive_bayes_model.pkl", 'rb'))

### Vactorize test text data
def tfidf_vec(test_text):
    print("test_text",test_text)
    X_tf1 = tf1.transform([test_text])
    return X_tf1


### predict Patient category
def predict_category(test_text):
    clean_text=preprocessing(test_text)
    x_test_tfidf=tfidf_vec(clean_text)
    y_test_pred = model.predict(x_test_tfidf)
    if y_test_pred==0:
        category="Not a Patient"
    else:
        category = "Patient"
    return category


if __name__ == '__main__':
    t="feeling dizzyness and vomit"
    y=predict_category(t)
    print(y)
