import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer , TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.decomposition import NMF
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import nltk
from gensim import matutils, models
import scipy.sparse
from sklearn.pipeline import Pipeline
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()

nltk.download('averaged_perceptron_tagger')

def english_nouns(text):
    pos = nltk.pos_tag(word_tokenize(text))
    noun_list = ''
    for i in range(len(pos)):
        if pos[i][1] == "NN":
            noun_list += pos[i][0] + " "
    return noun_list

def extract_nouns_en(df):
    df['nouns_only'] = df['noun_text'].apply(lambda x: english_nouns(x))

def display_topics(model, feature_names, no_top_words, topic_names=None):
    """
    Displays the top n terms in each topic
    """
    for ix, topic in enumerate(model.components_):
        if not topic_names or not topic_names[ix]:
            print("\nTopic ", ix + 1)
        else:
            print("\nTopic: '",topic_names[ix],"'")
        print(", ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]]))