import pandas as pd
import numpy as np
import string
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer



def pre_process(text):
    text = text.lower()
    ## remove punctuation
    pun = string.punctuation
    pun = string.punctuation
    text = text.translate(str.maketrans(" "," ",pun))

    text = text.split(" ")
    ## remove stop words
    stop_words = stopwords.words("english")
    text = [word for word in text if word not in stop_words]

    return " ".join(text)

def update_df(df):
    df['course_title'] = df['course_title'].apply(lambda x:pre_process(x))
    return df

def get_consing_mat(df):
    cv = CountVectorizer()
    cvmat = cv.fit_transform(df['course_title'])
    cos_sim = cosine_similarity(cvmat)

    return cos_sim


def extract_feature(df):
    course_title = list(df['course_title'])
    course_url = list(df['url'])
    
    return course_title,course_url