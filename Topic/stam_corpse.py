import gensim
import numpy as np
import spacy
from spacy import displacy
from gensim.corpora import Dictionary
from gensim.models import LdaModel
import matplotlib.pyplot as plt
import sklearn
file="corpse1.csv"
file_handle=open(file,'r')

nlp = spacy.load('en_core_web_sm')
for line in file_handle:
    text=line
    text=text[:-1]
    text=' '.join(text.split('\n'))
    text=' '.join(text.split())
    text=text+"\n"
    doc = nlp(text.lower())
    texts, article = [], []
    for w in doc:
        if w.text != '\n' and not w.is_stop and not w.is_punct and not w.like_num and w.text != 'I':    
            article.append(w.lemma_)
        if w.text == '\n':
            texts.append(article)
            article = []
    for i in texts:
        for j in i:
            print(j,end=" ")
        print()
