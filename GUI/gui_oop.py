import tkinter
from  tkinter import *
from tkinter import filedialog
import sys
sys.path.insert(0,'/home/rahulranjan/TextMiner/Processor')
import namedEntity
import partofSpeech
import sentTokenize
import wordTokenize

class gui:
 

 def __init__(self):
  self.maindisplay()
  

 def maindisplay(self):
  self.root = Tk()
  self.root.minsize(250, 250)
  self.root.title("TextMiner")
  self.icon = tkinter.Image("photo", file="/home/rahulranjan/TextMiner/Data/icon.gif")
  self.root.tk.call('wm','iconphoto',self.root._w,self.icon)
  self.browseButton()
  self.neButton()
  self.posButton()
  self.stButton()
  self.wtButton()
  self.root.mainloop()
 

 def browseButton(self):
  browseButton = Button(self.root,text="Browse",bg="red",command=self.browse)
  browseButton.pack()
 

 def neButton(self):
  neButton=Button(self.root,text="NE Miner",bg="red",comman=self.namedEntity)
  neButton.pack()
 

 def posButton(self):
  posButton=Button(self.root,text="POS Tagger",bg="red",comman=self.partofSpeech)
  posButton.pack()
 

 def stButton(self):
  stButton=Button(self.root,text="Sent. Tokenize",bg="red",comman=self.sentTokenize)
  stButton.pack()
 

 def wtButton(self):
  wtButton=Button(self.root,text="Word Tokenize",bg="red",comman=self.wordTokenize)
  wtButton.pack()


 def browse(self):
  browse = Tk() 
  #browse.tk.call('wm','iconphoto',browse._w,self.icon)
  self.filename = filedialog.askopenfilename(initialdir = "/home/rahulranjan/TextMiner/Data",title = "Choose your file",filetypes = (("Text files","*.txt"),))
  self.name=self.filename.split('/')[-1]
  browse.destroy()
  self.docview()


 def docview(self):
  docview=Tk()
  #docview.tk.call('wm','iconphoto',docview._w,self.icon)
  docview.title("Document: "+self.name)
  myFile=open(self.filename,"r+")
  self.myText=myFile.read()
  myTextWidget=Text(docview)
  myTextWidget.insert(0.0,self.myText)
  myTextWidget.pack(fill=BOTH)
  docview.mainloop()

 
 def namedEntity(self):
  ne=Tk()
  #ne.tk.call('wm','iconphoto',ne._w,self.icon)
  ne.title("Named-Entity List: "+self.name)
  neWidget=Text(ne)
  ne_array=namedEntity.namedEntity(self.myText)
  for i in ne_array:
   neWidget.insert(0.0,i+"\n")		
  neWidget.pack(fill=BOTH)
  ne.mainloop()
 

 def partofSpeech(self):
  pos=Tk()
  #pos.tk.call('wm','iconphoto',pos._w,self.icon)
  pos.title("POS Tagged List: "+self.name)
  posWidget=Text(pos)
  pos_array=partofSpeech.partofSpeech(self.myText)
  for i in pos_array:
   posWidget.insert(0.0,i+"\n")		
  posWidget.pack(fill=BOTH)
  pos.mainloop()
 

 def sentTokenize(self):
  st=Tk()
  #st.tk.call('wm','iconphoto',st._w,self.icon)
  st.title("Tokenized Sentences List: "+self.name)
  stWidget=Text(st)
  st_array=sentTokenize.sentTokenize(self.myText)
  for i in st_array:
   stWidget.insert(0.0,i+"\n\n\n")		
  stWidget.pack(fill=BOTH)
  st.mainloop()
 

 def wordTokenize(self):
  wt=Tk()
  #wt.tk.call('wm','iconphoto',wt._w,self.icon)
  wt.title("Tokenized Words List: "+self.name)
  wtWidget=Text(wt)
  wt_array=wordTokenize.wordTokenize(self.myText)
  for i in wt_array:
   wtWidget.insert(0.0,i+"\n")		
  wtWidget.pack(fill=BOTH)
  wt.mainloop()

 def iconify(self,root):
  
  root.tk.call('wm','iconphoto',root._w,img)
 
  



mainWindow=gui()


