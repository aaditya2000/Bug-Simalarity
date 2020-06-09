

from gensim.test.utils import common_texts
from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaModel
from gensim.test.utils import datapath

def Sort_Tuple(tup):  
  
    # reverse = None (Sorts in Ascending order)  
    # key is set to sort using second element of  
    # sublist lambda has been used  
    tup.sort(key = lambda x: x[1])  
    return tup  
 # Create a corpus from a list of texts
# print(common_texts)
common_dictionary = Dictionary(common_texts)
common_corpus = [common_dictionary.doc2bow(text) for text in common_texts]

 # Train the model on the corpus.
lda = LdaModel(common_corpus, num_topics=4,id2word=common_dictionary)
temp_file = datapath("model")
lda.save(temp_file)
lda = LdaModel.load(temp_file)
for i in lda.show_topics():
    print(i)
print(lda)
other_texts = [ ['computer', 'time', 'graph'], ['survey', 'response', 'eps'], ['human', 'system', 'computer'],['i','sad'] ]
other_corpus = [common_dictionary.doc2bow(text) for text in other_texts]
# print(other_corpus)
for i in other_corpus:
    unseen_doc = i
    vector = lda[unseen_doc]
    print(Sort_Tuple(vector))
    
