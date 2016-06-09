import nltk

def nltkwordTokenize(text):
 word_array=set()
 for word in nltk.word_tokenize(text):
  word_array.add(word)
 return word_array