import tkinter
from  tkinter import *
from tkinter import filedialog
import os.path
import getpass
from tkinter import messagebox
sys.path.insert(0,'/home/'+getpass.getuser()+'/TextMiner/Processor')
import namedEntity
import partofSpeech
import sentTokenize
import wordTokenize
import MySQLdb

class gui:
 

 def __init__(self):
  self.maindisplay()
  

 def maindisplay(self):
  self.root = Tk()
  self.root.minsize(250, 250)
  self.root.title("TextMiner")
  self.icon = tkinter.Image("photo", file="/home/"+getpass.getuser()+"/TextMiner/Data/icon.png")
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
  neButton=Button(self.root,text="NE Miner",bg="red",command=self.namedEntity)
  neButton.pack()
 

 def posButton(self):
  posButton=Button(self.root,text="POS Tagger",bg="red",command=self.partofSpeech)
  posButton.pack()
 

 def stButton(self):
  stButton=Button(self.root,text="Sent. Tokenize",bg="red",command=self.sentTokenize)
  stButton.pack()
 

 def wtButton(self):
  wtButton=Button(self.root,text="Word Tokenize",bg="red",command=self.wordTokenize)
  wtButton.pack()

 def manualButton(self):
  manualButton=Button(self.root,text="Manual Annotate",bg="red",command=self.manual)
  manualButton.pack()

 def getManualButton(self):
  getManualButton=Button(self.root,text="Get Manual Annotations",bg="red",command=self.getManual)
  getManualButton.pack()


 def getPerson(self):
  db = MySQLdb.connect("localhost","root","","manual_annotations")
  cursor = db.cursor()
  sql = """SELECT name FROM annotations WHERE category = 'Person' """ 
  cursor.execute(sql)
  results = cursor.fetchall()
  for row in results:
    self.name = row[0]
    #print(self.name)
    self.highlightNew()
    
  db.commit()
 def highlightNew(self):
  try:
    search=self.name
    #print(search)
    search = " " + search + " "
    start=1.0
    first=self.T.search(search,1.0,stopindex=END)
    self.T.tag_configure("YELLOW", background="yellow")
    self.T.tag_remove("YELLOW", 1.0, "end")
    while first:
     row,col=first.split('.')
     col = int(col) + 1
     first = row+'.'+str(col)
     last=int(col)+len(search) - 2
     last=row+'.'+str(last)
     row,col=last.split('.') 
     print(first)
     print(last)
     self.T.tag_add("YELLOW", first,last)
     start=last
     first=self.T.search(search,start,stopindex=END)
  except:
    print(self.name)
    start=1.0
    first=self.T.search(search,1.0,stopindex=END)
    print("exception Not")
    abc = ''
 def browse(self):

  self.filename = filedialog.askopenfilename(initialdir = "/home/"+getpass.getuser()+"/TextMiner/Data",title = "Choose your file",filetypes = (("Text files","*.txt"),))
  self.name=(self.filename.split('/')[-1]).split('.')[0]
  self.docview()

 def docview(self):
  self.root=Tk()
  #docview.tk.call('wm','iconphoto',docview._w,self.icon)
  #self.icon = tkinter.Image("photo", file="/home/sravan/TextMiner/Data/icon.png")
  #self.root.tk.call('wm','iconbitmap',self.root._w,self.icon)
  #self.root.iconbitmap(r'/home/sravan/TextMiner/Data/images.jpg')
  docview = self.root
  
  docview.title("Document: "+self.name)
  f=open(self.filename,"r+")
  data = f.read()
  self.myText=data
  S = Scrollbar(docview)
  T = Text(docview,height=20)
  self.T = T
  S.pack(side=RIGHT,fill=Y)
  T.pack(expand = 1, fill= BOTH)
  S.config(command=T.yview)
  T.config(yscrollcommand=S.set)
  T.insert(END,data)
  T.config(state=DISABLED)
  getPersonButton=Button(self.root,text="Get Person Annotated",bg="red",command=self.getPerson)
  getPersonButton.pack()
  docview.mainloop()

 
 def namedEntity(self):  #ne.tk.call('wm','iconphoto',ne._w,self.icon)
  if hasattr(self, 'filename'):
    ne=Tk()

    ne.title("Named-Entity List: "+self.name)
    neWidget=Text(ne)
    ne_array=namedEntity.namedEntity(self.myText)
    string=""
    for i in ne_array:
     string = string + i + "\n"
    data = string
    S = Scrollbar(ne)
    T = Text(ne,height=20)
    S.pack(side=RIGHT,fill=Y)
    T.pack(expand = 1, fill= BOTH)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    T.insert(END,data)
    T.config(state=DISABLED)
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
    string = ""
    for i in pos_array:
      string = string + i + "\n"
    data = string  
    S = Scrollbar(pos)
    T = Text(pos,height=20)
    S.pack(side=RIGHT,fill=Y)
    T.pack(expand = 1, fill= BOTH)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    T.insert(END,data)
    T.config(state=DISABLED)
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
    string = ""
    for i in st_array:
      string = string + i + "\n"
    data = string  
    S = Scrollbar(st)
    T = Text(st,height=20)
    S.pack(side=RIGHT,fill=Y)
    T.pack(expand = 1, fill= BOTH)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    T.insert(END,data)
    T.config(state=DISABLED)
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
    string = ""
    for i in wt_array:
      string = string + i + "\n"
    data = string  
    S = Scrollbar(wt)
    T = Text(wt,height=20)
    S.pack(side=RIGHT,fill=Y)
    T.pack(expand = 1, fill= BOTH)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    T.insert(END,data)
    T.config(state=DISABLED)      
    wt.mainloop()
  else:
    content = "Please Select a File"
    messagebox.showinfo("Error! Oops",content)


 def manual(self):
  if hasattr(self,'filename'):
    self.manual=Tk()
    self.manual.title("Manually Annotate: "+self.name)
    self.manualWidget=Text(self.manual)
    self.manualWidget.insert(0.0,self.myText)
    self.manualWidget.pack(expand = 1, fill= BOTH)
    label_1=Label(self.manual,text="Word")
    label_2=Label(self.manual,text="Category")
    self.entry_1=Entry(self.manual)
    self.entry_2=Entry(self.manual)
    label_1.pack()
    label_2.pack()
    self.entry_1.pack()
    self.entry_2.pack()
    self.manual_array=set()
    self.entry_3=Entry(self.manual)
    self.entry_3.pack()
    submit=Button(self.manual,text="Submit",bg="red",command=self.submit)
    submit.pack()
    done=Button(self.manual,text="Done",bg="red",command=self.done)
    done.pack()
    highlight=Button(self.manual,text="HIGHLIGHT",bg="red",command=self.highlight)
    highlight.pack()
    self.manual.mainloop()
  else:
    content = "Please Select a File"
    messagebox.showinfo("Error! Oops",content)

 def highlight(self):

  try:
    search=self.entry_3.get()
    search = " " + search + " "
    start=1.0
    first=self.manualWidget.search(search,1.0,stopindex=END)
    self.manualWidget.tag_configure("YELLOW", background="yellow")
    self.manualWidget.tag_remove("YELLOW", 1.0, "end")
    while first:
     row,col=first.split('.')
     col = int(col) + 1
     first = row+'.'+str(col)
     last=int(col)+len(search) - 2
     last=row+'.'+str(last)
     row,col=last.split('.') 
     print(first)
     print(last)
     self.manualWidget.tag_add("YELLOW", first,last)
     start=last
     first=self.manualWidget.search(search,start,stopindex=END)
  except:
    content = "Please Enter a text in highlight box"
    messagebox.showinfo("Error! Oops",content)



 def submit(self):
  db = MySQLdb.connect("localhost","root","","manual_annotations")
  cursor = db.cursor()
  var1 = self.entry_1.get()
  print(var1)
  var2 = self.entry_2.get()
  sql = "INSERT INTO annotations(name, \
         category) \
         VALUES ('%s','%s')" % \
         (var1,var2)
  cursor.execute(sql)
  db.commit()
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
    manualAnnotWidget.pack(expand = 1, fill= BOTH)
    manualAnnot.mainloop()
  else:
    content = "Please Select a File"
    messagebox.showinfo("Error! Oops",content)

 """def getfromDict(self):
  self.dic=Tk()
  self.dic.title("Dictionary Highlight: "+self.name)
  self.dicWidget=Text(self.dic)
  self.dicWidget.insert(0.0,self.myText)
  self.manualWidget.pack(expand = 1, fill= BOTH)
  browseDicButton = Button(self.dic,text="Browse Dictionary",bg="red",command=self.browsedic)
  browseDicButton.pack()
  highlightdic=Button(self.manual,text="HIGHLIGHT",bg="red",command=self.highlightdic)
  highlightdic.pack()
   
 def browsedic(self):
  self.dictname = filedialog.askopenfilename(initialdir = "/home/"+getpass.getuser()+"/TextMiner/Data",title = "Choose your file",filetypes = (("Text files","*.txt"),))
"""
    




mainWindow=gui()


