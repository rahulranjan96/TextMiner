import nltk

def sentTokenize(Text):
	sent_array=set()
	for sent in sent_tokenize(text):
		sent_array.add(sent)
    return sent_array