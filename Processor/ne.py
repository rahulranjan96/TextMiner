"""import nltk 
def extract_entities(text):
     for sent in nltk.sent_tokenize(text):
         tokens = nltk.word_tokenize(sent)
         tagged_tokens=nltk.pos_tag(tokens)
         print(tagged_tokens)
         print("\n\n\n\n\n")
f=open("sample.txt","r+")
sample = f.read()
extract_entities(sample)"""


"""import nltk
sentence = 'Python has a wonderful open-source library for performing NLP (natural language processing) on text. This library is called the Natural Language Toolkit (NLTK). '
sent=nltk.sent_tokenize(sentence)
for i in sent:
    tokens = nltk.word_tokenize(i)
    tagged_tokens=nltk.pos_tag(tokens)
    print(tagged_tokens)"""
"""tokens = nltk.word_tokenize(sent)
tagged_tokens = nltk.pos_tag(tokens)
print(tagged_tokens)"""

"""import nltk
tokens = nltk.word_tokenize('President Barack Obama is the 44th President of the United States of America.')
tokens = nltk.pos_tag(tokens)
tree = nltk.ne_chunk(tokens)
if(hasattr(tree,'label')):
    print(tree)"""

import nltk

def extract_entities(text):
    ne_array=set()
    for sent in nltk.sent_tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label'):
               string="Word(with POS tagging): "+str(chunk.leaves()) + ' , ' + "Category: "+chunk.label()
               ne_array.add(string)
    return ne_array 
                #print("\n")
                #print (chunk.label, ' '.join(c[0] for c in chunk.leaves()))


