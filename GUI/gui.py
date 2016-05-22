
"""
from nltk.tokenize import sent_tokenize, word_tokenize

root = Tk()
myTextWidget=Text(root,bg="red")
myFile=open("sampletext.txt","r")
myText=myFile.read()
array=word_tokenize(myText)
myFile.close()
for i in array:
 myTextWidget.insert(0.0,i)
myTextWidget.pack(fill=BOTH)

root.mainloop()

""" 
from  tkinter import *
from tkinter import filedialog
from functools import partial
from nltk.tokenize import sent_tokenize, word_tokenize

def process(myText,root):
 myTextWidget=Text(root)
 array=word_tokenize(myText) 
 for i in array:
  myTextWidget.insert(0.0,i)
  myTextWidget.insert(0.0,"\n")
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