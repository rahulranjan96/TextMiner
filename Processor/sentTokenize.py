from nltk import *

def sentTokenize(text):
 sent_array=set()
 for sent in sent_tokenize(text):
  sent_array.add(sent)
 return sent_array