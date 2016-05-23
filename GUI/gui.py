from  tkinter import *
from tkinter import filedialog
from functools import partial
from nltk.tokenize import word_tokenize,sent_tokenize
import nltk

def process(myText,root):
 myTextWidget=Text(root)
 array=sent_tokenize(myText)
 for i in array:
  words=word_tokenize(i)
  tagged=nltk.pos_tag(words)
  namedEnt=nltk.ne_chunk(tagged)
  myTextWidget.insert(0.0,namedEnt)
  myTextWidget.insert(0.0,"\n\n\n")
 myTextWidget.pack(fill=BOTH)
 
def readfile(root):
 root1 = Tk() 
 filename = filedialog.askopenfilename(initialdir = "/home",title = "Choose your file",filetypes = (("Text files","*.txt"),))
 myFile=open(filename,"r")
 myText=myFile.read()
 myTextWidget=Text(root)
 myTextWidget.insert(0.0,myText)
 myTextWidget.pack(fill=BOTH)
 process_but = Button(root,text="Process",fg="red",command=partial(process,myText,root))
 process_but.pack()
 root1.withdraw()



root = Tk()
readfiles = partial(readfile,root)
browse = Button(root,text="Browse",fg="red",command=readfiles)
browse.pack()
root.mainloop()