from nltk import *

def wordTokenize(text):
 word_array=set()
 for word in word_tokenize(text):
  word_array.add(word)
 return word_array