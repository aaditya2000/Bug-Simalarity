import gensim
import numpy as np
import spacy
from spacy import displacy
from gensim.corpora import Dictionary
from gensim.models import LdaModel
import matplotlib.pyplot as plt
from gensim.test.utils import datapath
import sklearn
def Sort_Tuple(tup):   
    tup.sort(key = lambda x: x[1])  
    return tup
file = "corpse_1.csv"
file_handle=open(file,'r')
nlp = spacy.load('en_core_web_sm')


text=file_handle.read()
doc = nlp(text.lower())
texts, article = [], []
for w in doc:
    if w.text != '\n' and not w.is_stop and not w.is_punct and not w.like_num and w.text != 'I':
        article.append(w.lemma_)
    if w.text == '\n':
        texts.append(article)
        article = []
dictionary = Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
if len(corpus) == 0 :
    print()
else:
    ldamodel = LdaModel(corpus=corpus, num_topics=50, id2word=dictionary)
    temp_topic_file = datapath("model")
    ldamodel.save(temp_topic_file)
    ldamodel = LdaModel.load(temp_topic_file)
    # print(ldamodel)
    # for i in ldamodel.show_topics():
    #     print(i)
    

file="sample.csv"
print("issue_id,topic")
file_handle=open(file,'r')
file_handle.readline()
for line in file_handle:
    a,text=line.split("~",1)
    text=text[:-1]
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
    bigram = gensim.models.Phrases(texts)
    texts = [bigram[line] for line in texts]
    other_corpus = [dictionary.doc2bow(text) for text in texts]
    # print(other_corpus)
    if(len(other_corpus)==0):
        print("Fuckk off")
    else:
        list=[]
        for i in other_corpus:
            unseen_doc = i
            list+=ldamodel[unseen_doc]
    
        list=Sort_Tuple(list)
        x=0
        for i in list:
            print(str(a)+","+str(i[0]))
            x+=1
            if(x==3):
                break


    
