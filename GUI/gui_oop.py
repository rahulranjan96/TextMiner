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
  scrollbar = Scrollbar(self.root)
  scrollbar.pack(side = RIGHT,fill=Y)
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
  self.filename = filedialog.askopenfilename(initialdir = "/home/rahulranjan/TextMiner/Data",title = "Choose your file",filetypes = (("Text files","*.txt"),))
  self.docview()
  browse.destroy()


 def docview(self):
  myFile=open(self.filename,"r+")
  self.myText=myFile.read()
  myTextWidget=Text(self.root)
  myTextWidget.insert(0.0,self.myText)
  myTextWidget.pack(fill=BOTH)

 
 def namedEntity(self):
  ne=Tk()
  neWidget=Text(ne)
  scrollbar = Scrollbar(ne)
  scrollbar.pack(side = RIGHT,fill=Y)
  ne_array=namedEntity.namedEntity(self.myText)
  for i in ne_array:
   neWidget.insert(0.0,i+"\n")		
  neWidget.pack(fill=BOTH)
  ne.mainloop()
 

 def partofSpeech(self):
  pos=Tk()
  posWidget=Text(pos)
  scrollbar = Scrollbar(pos)
  scrollbar.pack(side = RIGHT,fill=Y)
  pos_array=partofSpeech.partofSpeech(self.myText)
  for i in pos_array:
   posWidget.insert(0.0,i+"\n")		
  posWidget.pack(fill=BOTH)
  pos.mainloop()
 

 def sentTokenize(self):
  st=Tk()
  stWidget=Text(st)
  scrollbar = Scrollbar(st)
  scrollbar.pack(side = RIGHT,fill=Y)
  st_array=sentTokenize.sentTokenize(self.myText)
  for i in st_array:
   stWidget.insert(0.0,i+"\n")		
  stWidget.pack(fill=BOTH)
  st.mainloop()
 

 def wordTokenize(self):
  wt=Tk()
  wtWidget=Text(wt)
  scrollbar = Scrollbar(wt)
  scrollbar.pack(side = RIGHT,fill=Y)
  wt_array=wordTokenize.wordTokenize(self.myText)
  for i in wt_array:
   wtWidget.insert(0.0,i+"\n")		
  wtWidget.pack(fill=BOTH)
  wt.mainloop()

 
 
  



mainWindow=gui()


