import gensim
import nltk
from nltk.stem.porter import *
import numpy as np
import spacy
stemmer = PorterStemmer()
from spacy import displacy
from gensim.corpora import Dictionary
from gensim.models import LdaModel
import matplotlib.pyplot as plt
import sklearn
file=input()
file_handle=open(file,'r')
file_handle.readline()
print("issue_id~stam_let")
nlp = spacy.load('en_core_web_sm')

for line in file_handle:
    a,text=line.split("~",1)
    text=text[:-1]
    text=' '.join(text.split('\n'))
    text=' '.join(text.split())
    text=text+"\n"
    doc = nlp(text.lower())
    texts, article = [], []
    for w in doc:
        if w.text != '\n' and not w.is_stop and not w.is_punct and not w.like_num and w.text != '-' and w.text!='I':
            article.append(stemmer.stem(w.lemma_))
        if w.text == '\n':
            texts.append(article)
            article = []
    print(a,end="~")
    for i in texts:
        for j in i:
            print(j,end=" ")
    print()
