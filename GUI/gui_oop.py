import tkinter
from  tkinter import *
from tkinter import filedialog
import os.path
import sys
from tkinter import messagebox
sys.path.insert(0,'/home/sravan/TextMiner/Processor')
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
  self.icon = tkinter.Image("photo", file="/home/sravan/TextMiner/Data/icon.png")
  self.root.tk.call('wm','iconphoto',self.root._w,self.icon)
  self.browseButton()
  self.neButton()
  self.posButton()
  self.stButton()
  self.wtButton()
  self.manualButton()
  self.getManualButton()
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

 def manualButton(self):
  manualButton=Button(self.root,text="Manual Annotate",bg="red",comman=self.manual)
  manualButton.pack()

 def getManualButton(self):
  getManualButton=Button(self.root,text="Get Manual Annotations",bg="red",comman=self.getManual)
  getManualButton.pack()


 def browse(self):
  self.filename = filedialog.askopenfilename(initialdir = "/home/sravan/TextMiner/Data",title = "Choose your file",filetypes = (("Text files","*.txt"),))
  self.name=(self.filename.split('/')[-1]).split('.')[0]
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

 
 def namedEntity(self):  #ne.tk.call('wm','iconphoto',ne._w,self.icon)
  if hasattr(self, 'filename'):
    ne=Tk()
    ne.title("Named-Entity List: "+self.name)
    neWidget=Text(ne)
    ne_array=namedEntity.namedEntity(self.myText)
    for i in ne_array:
     neWidget.insert(0.0,i+"\n")    
    neWidget.pack(fill=BOTH)
    ne.mainloop()
  else:
    content = "Please Select a File"
    messagebox.showinfo("Error! Oops",content)
 
 def partofSpeech(self):
  #pos.tk.call('wm','iconphoto',pos._w,self.icon)
  if hasattr(self,'filename'):
    pos=Tk()
    pos.title("POS Tagged List: "+self.name)
    posWidget=Text(pos)
    pos_array=partofSpeech.partofSpeech(self.myText)
    for i in pos_array:
      posWidget.insert(0.0,i+"\n")    
    posWidget.pack(fill=BOTH)
    pos.mainloop()
  else:
    content = "Please Select a File"
    messagebox.showinfo("Error! Oops",content)

 

 def sentTokenize(self):
  #st.tk.call('wm','iconphoto',st._w,self.icon)
  if hasattr(self,'filename'):
    st=Tk()
    st.title("Tokenized Sentences List: "+self.name)
    stWidget=Text(st)
    st_array=sentTokenize.sentTokenize(self.myText)
    for i in st_array:
      stWidget.insert(0.0,i+"\n\n\n")   
      stWidget.pack(fill=BOTH)
      st.mainloop()
  else:
    content = "Please Select a File"
    messagebox.showinfo("Error! Oops",content)
 def wordTokenize(self):
  #wt.tk.call('wm','iconphoto',wt._w,self.icon)
  if hasattr(self,'filename'):
    wt=Tk()
    wt.title("Tokenized Words List: "+self.name)
    wtWidget=Text(wt)
    wt_array=wordTokenize.wordTokenize(self.myText)
    for i in wt_array:
      wtWidget.insert(0.0,i+"\n")   
      wtWidget.pack(fill=BOTH)
      wt.mainloop()
  else:
    content = "Please Select a File"
    messagebox.showinfo("Error! Oops",content)


 def manual(self):
  if hasattr(self,'filename'):

    self.manual=Tk()
    #docview.tk.call('wm','iconphoto',docview._w,self.icon)
    self.manual.title("Manually Annotate: "+self.name)
    self.manualWidget=Text(self.manual)
    self.manualWidget.insert(0.0,self.myText)
    self.manualWidget.pack(fill=BOTH)
    label_1=Label(self.manual,text="Word")
    label_2=Label(self.manual,text="Category")
    self.entry_1=Entry(self.manual)
    self.entry_2=Entry(self.manual)
    label_1.pack()
    label_2.pack()
    self.entry_1.pack()
    self.entry_2.pack()
    self.manual_array=set()
    submit=Button(self.manual,text="Submit",bg="red",command=self.submit)
    submit.pack()
    done=Button(self.manual,text="Done",bg="red",command=self.done)
    done.pack()

    self.manual.mainloop()
  else:
    content = "Please Select a File"
    messagebox.showinfo("Error! Oops",content)


 def submit(self):
  self.manual_array.add(self.entry_1.get()+"~"+self.entry_2.get())
 
 def done(self):
  f = open(self.name + "_manualAnnot.txt","w")
  for i in self.manual_array:
   f.write(i)
   f.write("\n")
  self.manual.destroy()
    
 def getManual(self):
  if hasattr(self,'filename'):

    manualAnnot=Tk()
    manualAnnot.title("Manual Annotate: "+self.name)
    manualFile=open(self.name + "_manualAnnot.txt","r+")
    manualText=manualFile.read()
    manualAnnotWidget=Text(manualAnnot)
    manualAnnotWidget.insert(0.0,manualText)
    manualAnnotWidget.pack(fill=BOTH)
    manualAnnot.mainloop()
  else:
    content = "Please Select a File"
    messagebox.showinfo("Error! Oops",content)

  



mainWindow=gui()


