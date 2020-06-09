import gensim
import numpy as np
import spacy
from spacy import displacy
from gensim.corpora import Dictionary
from gensim.models import LdaModel
import matplotlib.pyplot as plt
import sklearn
# import keras
# file =input()
file="sample.csv"
file_handle=open(file,'r')
file_handle.readline()
nlp = spacy.load('en_core_web_sm')

for line in file_handle:
    a,text=line.split("~",1)
    text=text[:-1]
    text=' '.join(text.split())
    text=text+"\n"
    # print(text)

    doc = nlp(text.lower())
    # print(doc)
    # sent = nlp(u"Tom ran to the repair shop to fix his bicycle.")


    # for token in sent:
    #     print(token.text, token.pos_, token.tag_)


    # we add some words to the stop word list
    texts, article = [], []
    for w in doc:
        # if it's not a stop word or punctuation mark, add it to our article!
        if w.text != '\n' and not w.is_stop and not w.is_punct and not w.like_num and w.text != 'I':
            # we add the lematized version of the word
            article.append(w.lemma_)
        # if it's a new line, it means we're onto our next document
        if w.text == '\n':
            texts.append(article)
            article = []
    # for i in texts:
    #     print(i)

    bigram = gensim.models.Phrases(texts)
    texts = [bigram[line] for line in texts]
    # print(texts)
    dictionary = Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    if len(corpus) == 0 :
        print("fadssf")
    else:
        ldamodel = LdaModel(corpus=corpus, num_topics=3, id2word=dictionary)

        for i in ldamodel.show_topics():
            ans=' '.join(i[1].split(" + "))
            # ans=' '.join(ans.split('*'))
            ans=''.join(ans.split('"'))
            


            print(a+"~"+ans)