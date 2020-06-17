from pymongo import MongoClient
from pprint import pprint
import nltk
import re
import string
import pandas as pd
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.lancaster import LancasterStemmer
import nltk
nltk.download('wordnet')
lemmatizer = nltk.stem.WordNetLemmatizer()

def clean_content(df_list):
    for i in range(len(df_list)):
        df_list[i]['Content'] = df_list[i]['Content'].apply(lambda x: cleaner(x))nltk.stem import WordNetLemmatizer

def cleaner(text):
    """
    Arguments: text to clean
    Output: removes HTML, removes punctuation, makes text lowercase, removes numbers"""
    soup = BeautifulSoup(text, 'lxml')
    html_free = soup.get_text()
    clean_text = re.sub('[%s]' % re.escape(string.punctuation), '', html_free)
    clean_text = clean_text.lower()
    clean_text = re.sub('\w*\d\w*', '', clean_text)
    return clean_text



def add_word_tokenized_column(df_list):
    for i in range(len(df_list)):
        df_list[i]['word_tokenized'] = df_list[i].apply(lambda row: nltk.word_tokenize(row['Content']), axis=1)

def stem_text(text):
    stemmer = LancasterStemmer()
    return [stemmer.stem(word) for word in text]

def add_stem_column(df_list):
    for i in range(len(df_list)):
        df_list[i]['stemmed_text'] = df_list[i]['word_tokenized'].apply(lambda x: stem_text(x))

def lemmatize_nouns(text):
    lemmatized = [lemmatizer.lemmatize(word, pos="n") for word in text]
    return lemmatized

def lemmatize_verbs(text):
    lemmatized = [lemmatizer.lemmatize(word, pos="v") for word in text]
    return lemmatized

def add_noun_column(df_list):
    for i in range(len(df_list)):
        df_list[i]['noun_text'] = df_list[i]['word_tokenized'].apply(lambda x: lemmatize_nouns(x))
        df_list[i]['noun_text'] = df_list[i]['noun_text'].apply(' '.join)

def add_verb_column(df_list):
    for i in range(len(df_list)):
        df_list[i]['verb_text'] = df_list[i]['word_tokenized'].apply(lambda x: lemmatize_verbs(x))
        df_list[i]['verb_text'] = df_list[i]['verb_text'].apply(' '.join)