import nltk

def nltksentTokenize(text):
 sent_array=set()
 for sent in nltk.sent_tokenize(text):
  sent_array.add(sent)
 return sent_array