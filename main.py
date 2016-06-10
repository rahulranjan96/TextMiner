import tkinter
from  tkinter import *
from tkinter import filedialog
import os.path
import getpass
import socket
from tkinter import messagebox
sys.path.insert(0,'/home/'+getpass.getuser()+'/TextMiner/Processor')
import nltknamedEntity
import nltkpartofSpeech
import nltksentTokenize
import nltkwordTokenize
import polyglotName
import polyglotSent
import polyglotWord
import polyglotSpeech
import MySQLdb
from functools import partial
from PIL import ImageTk
from PIL import Image





class gui:
 
 

 def __init__(self):
  self.customFont = ('Times', 20, 'bold')
  self.maindisplay()
  

 def maindisplay(self):
  root = Tk()
  root.minsize(1000,700)
  root.resizable(width=False, height=False)
  im = Image.open("/home/"+getpass.getuser()+"/TextMiner/Data/background.jpg")
  tkimage = ImageTk.PhotoImage(im)
  myvar=Label(root,image = tkimage)
  myvar.place(x=0, y=0, relwidth=1.0, relheight=1.0)
  var  = StringVar(root)
  self.er = var
  var.set("nltk")
  root.title("TextMiner")
  self.icon(root)
  self.browseButton(root)
  self.stButton(root)
  self.wtButton(root)
  self.posButton(root)
  self.neButton(root)
  self.manualButton(root)
  self.getManualButton(root)
  self.dictionaryButton(root)
  option = OptionMenu(root, var, "NLTK","POLYGLOT")
  option.config(width=8,height=2)
  option.place(x = 450, y = 550)
  self.getLibraryButton(root)
  root.mainloop()


 

 def browseButton(self,root):
  browseButton = Button(root,text="Browse",width=21,bg="red",font=self.customFont,command=partial(self.browse,root))
  browseButton.place(x = 400, y = 150)

 
 def stButton(self,root):
  stButton=Button(root,text="Sentence Tokenizer",width=21,bg="red",font=self.customFont,command=self.sentTokenizechecker)
  stButton.place(x = 400, y = 200)

 
 def wtButton(self,root):
  wtButton=Button(root,text="Word Tokenizer",width=21,bg="red",font=self.customFont,command=self.wordTokenizechecker)
  wtButton.place(x = 400, y = 250)


 def posButton(self,root):
  posButton=Button(root,text="POS Tagger",width=21,bg="red",font=self.customFont,command=self.partofSpeechchecker)
  posButton.place(x = 400, y = 300)


 def neButton(self,root):
  neButton=Button(root,text="Named Entity Recognizer",width=21,bg="red",font=self.customFont,command=self.namedEntitychecker)
  neButton.place(x = 400, y = 350)


 def manualButton(self,root):
  manualButton=Button(root,text="Manually Annotate",width=21,bg="red",font=self.customFont,command=self.manual)
  manualButton.place(x = 400, y = 400)


 def getManualButton(self,root):
  getManualButton=Button(root,text="Get Manual Annotations",width=21,bg="red",font=self.customFont,command=self.getManual)
  getManualButton.place(x = 400, y = 450)


 def dictionaryButton(self,root):
  dictionaryButton = Button(root,text="Give Dictionary",width=21,bg="red",font=self.customFont,command=self.dictionary)
  dictionaryButton.place(x = 400, y = 500)


 def getLibraryButton(self,root):
  okbutton = Button(root,text="OK",bg="green",font=self.customFont,command=self.ok)
  okbutton.place(x = 550, y = 550)



 def sentTokenizechecker(self):
  if hasattr(self, "name"):
    if hasattr(self, "value"):
      if(self.value==0):
       self.sentTokenizeNLTK()
       print("NLTK")
      else:
        print("POLYGLOT")
        self.sentTokenizePolyglot()
    else:
     self.sentTokenizeNLTK()
  else:
    content = "Please Select a File"
    messagebox.showinfo("Error! Oops",content)
 

 def wordTokenizechecker(self):
  if hasattr(self,"name"):
    if hasattr(self,"value"):
      if(self.value==0):
        self.wordTokenizeNLTK()
        print("NLTK")
      else:
        print("POLYGLOT")
        self.wordTokenizePolyglot()
    else:
      self.wordTokenizeNLTK()
  else:
    content = "Please select a  file"
    messagebox.showinfo("Error! Ooops",content)


 def partofSpeechchecker(self):
  if hasattr(self,"name"):
    if hasattr(self,"value"):
      if(self.value==0):
        self.partofSpeechNLTK()
        print("NLTK")
      else:
        print("POLYGLOT")
        self.partofSpeechPolyglot()
    else:
      self.partofSpeechNLTK()
  else:
    content = "Please select a file"
    messagebox.showinfo("Error Oops",content)


 def namedEntitychecker(self):
  if hasattr(self,"name"):
    if hasattr(self,"value"):
      if(self.value==0):
        self.namedEntityNLTK()
        print("NLTK")
      else:
        print("POLYGLOT")
        self.namedEntityPolyglot()
    else:
      self.namedEntityNLTK()
  else:
    content = "Please select a file"
    messagebox.showinfo("Error! Ooops",content)



 def sentTokenizeNLTK(self):
  if hasattr(self,'name'):
    st=Toplevel() 
    st.title("Tokenized Sentences List with NLTK: "+self.name)
    self.icon(st)
    stWidget=Text(st)
    st_array=nltksentTokenize.nltksentTokenize(self.myText)
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
    #st.mainloop()
  else:
    content = "Please Select a File"
    messagebox.showinfo("Error! Oops",content)


 def wordTokenizeNLTK(self):
  if hasattr(self,'name'):
    wt=Toplevel() 
    wt.title("Tokenized Words List with NLTK:: "+self.name)
    self.icon(wt)
    wtWidget=Text(wt)
    wt_array=nltkwordTokenize.nltkwordTokenize(self.myText)
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
    #wt.mainloop()
  else:
    content = "Please Select a File"
    messagebox.showinfo("Error! Oops",content)


 def partofSpeechNLTK(self):
  if hasattr(self,'name'):
    pos=Toplevel() 
    pos.title("Part of Speech tagging with NLTK: "+self.name)
    self.icon(pos)
    posWidget=Text(pos)
    pos_array=nltkpartofSpeech.nltkpartofSpeech(self.myText)
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
    #pos.mainloop()
  else:
    content = "Please Select a File"
    messagebox.showinfo("Error! Oops",content)



 def namedEntityNLTK(self):  
  if hasattr(self, 'name'):
    ne=Toplevel() 
    ne.title("Word Tokenization with NLTK: "+self.name)
    self.icon(ne)
    neWidget=Text(ne)
    ne_array=nltknamedEntity.nltknamedEntity(self.myText)
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
    #ne.mainloop()
  else:
    content = "Please Select a File"
    messagebox.showinfo("Error! Oops",content)

 

 def sentTokenizePolyglot(self):
  polyglotsent = Toplevel() 
  polyglotsent.title("Tokenized Sentences List with PolyGlot : "+self.name)
  self.icon(polyglotsent)
  data = self.myText
  sent_array = polyglotSent.polySentTokenize(data)
  string=""
  for i in sent_array:
    string = string + str(i) + "\n"
  data = string
  S = Scrollbar(polyglotsent)
  T = Text(polyglotsent,height=20)
  S.pack(side=RIGHT,fill=Y)
  T.pack(expand = 1, fill= BOTH)
  S.config(command=T.yview)
  T.config(yscrollcommand=S.set)
  T.insert(END,data)
  T.config(state=DISABLED)
  #polyglotsent.mainloop()


 def wordTokenizePolyglot(self):
  polyglotWordWin = Toplevel() 
  polyglotWordWin.title("Word Tokenization with Polyglot: "+self.name)
  self.icon(polyglotWordWin)
  data = self.myText
  word_array = polyglotWord.polyWordTokenize(data)
  string=""
  for i in word_array:
    string = string + str(i) + "\n"
  data = string
  S = Scrollbar(polyglotWordWin)
  T = Text(polyglotWordWin,height=20)
  S.pack(side=RIGHT,fill=Y)
  T.pack(expand = 1, fill= BOTH)
  S.config(command=T.yview)
  T.config(yscrollcommand=S.set)
  T.insert(END,data)
  T.config(state=DISABLED)
  #polyglotWordWin.mainloop()


 def partofSpeechPolyglot(self):
  polySpeechWin = Toplevel() 
  polySpeechWin.title("Part of Speech Tagging with Polyglot :"+self.name)
  self.icon(polySpeechWin)
  data = self.myText
  speech_array = polyglotSpeech.polySpeechTokenize(data)
  count = 1
  string = ""
  for i in speech_array:
    if(count%2==1):
      count = count + 1
      string = string + str(i) + "\t"
    else:
      count = count + 1
      string = string + str(i) + "\n"
  data = string
  S = Scrollbar(polySpeechWin)
  T = Text(polySpeechWin,height=20)
  S.pack(side=RIGHT,fill=Y)
  T.pack(expand = 1, fill= BOTH)
  S.config(command=T.yview)
  T.config(yscrollcommand=S.set)
  T.insert(END,data)
  T.config(state=DISABLED)
  #polySpeechWin.mainloop()


 def namedEntityPolyglot(self):
  #polyglotName = Tk()
  polyglotNameWin = Toplevel() 
  polyglotNameWin.title("Named Entity Recognition with PolyGlot : "+self.name)
  self.icon(polyglotNameWin)
  data = self.myText
  name_array = polyglotName.polyNameTokenize(data)
  #name_array = polyglotName.polyNameTokenize(data)
  var = 1
  count=1
  string=""
  for i in name_array:
   if(i=="000000"):
      var = 1
      if(count!=1):
        string = string + "\n"
      else:
        count = count+1
        ac = ""
   elif(var==1):
      count = count + 1
      i = i.split('-')
      string = string +  i[1] + ":"
      var = 0
   else:
      string = string + i + " "
  print(string)
  data = string
  S = Scrollbar(polyglotNameWin)
  T = Text(polyglotNameWin,height=20)
  S.pack(side=RIGHT,fill=Y)
  T.pack(expand = 1, fill= BOTH)
  S.config(command=T.yview)
  T.config(yscrollcommand=S.set)
  T.insert(END,data)
  T.config(state=DISABLED)
  #polyglotNameWin.mainloop()


 def browse(self,root):
  filename = filedialog.askopenfilename(initialdir = "/home/"+getpass.getuser()+"/TextMiner/Sample Text",title = "Choose your file",filetypes = (("Text files","*.txt"),))
  self.name=(filename.split('/')[-1]).split('.')[0]
  self.docview(filename,root)


 def ok(self):
  vare = self.er
  a = vare.get()
  if(a=="NLTK"):
    print(a)
    self.value=0
  elif(a=="POLYGLOT"):
    print(a)
    self.value=1
  else:
    print("NLP")
  print(self.value)


 def docview(self,filename,root):
  docview = Toplevel() 
  docview.title("Document: "+self.name)
  self.icon(docview)
  f=open(filename,"r+")
  data = f.read()
  self.myText=data
  S = Scrollbar(docview)
  docWidget = Text(docview,height=20)
  S.pack(side=RIGHT,fill=Y)
  docWidget.pack(expand = 1, fill= BOTH)
  S.config(command=docWidget.yview)
  docWidget.config(yscrollcommand=S.set)
  docWidget.insert(END,data)
  docWidget.config(state=DISABLED)
  getPersonButton=Button(docview,text="Get Person Annotated",bg="red",command=partial(self.getPerson,docWidget))
  getPersonButton.pack(side=LEFT)
  highlighDictionaryButton =Button(docview,text="Highlight Dictionary",bg="red",command=partial(self.highlightDictionary,docWidget))
  highlighDictionaryButton.pack(side=RIGHT)
  #docview.mainloop()


 def getPerson(self,widget):
  ip = socket.gethostbyname(self.gethostbyname())
  #if you want to connect to local database then in the place of 10.11.12.25 write ip
  #for Main Server Ip write the ip in the place of 10.11.12.25
  db = MySQLdb.connect("10.11.12.25","root","","manual_annotations")
  cursor = db.cursor()
  sql = """SELECT name FROM annotations WHERE category = 'Person' """ 
  cursor.execute(sql)
  results = cursor.fetchall()
  for row in results:
    name = row[0]
    self.highlight(name,widget,"yellow",1)
  db.commit()

 
 def dictionary(self):
  self.dicfileName = filedialog.askopenfilename(initialdir = "/home/"+getpass.getuser()+"/TextMiner/Sample Dictionary",title = "Choose your file",filetypes = (("Text files","*.txt"),))
  self.dicName=(self.dicfileName.split('/')[-1]).split('.')[0]
  with open(self.dicfileName) as fp:
    for line in fp:
      line = line.strip('\n')
      print(line)


 def highlightDictionary(self,widget):
  if hasattr(self, "dicfileName"):
    with open(self.dicfileName) as fp:
      for line in fp:
        line = line.strip('\n')
        self.highlight(line,widget,"green",1)
  else:
    content = "Please Select a File"
    messagebox.showinfo("Error! Oops",content)
 
 
 def manual(self):
  if hasattr(self,'name'):
    manual=Toplevel() 
    manual.title("Manually Annotate: "+self.name)
    self.icon(manual)
    manual.minsize(1200,1000)
    manual.resizable(width=False, height=False)
    manualWidget=Text(manual,height=20)
    manualWidget.insert(0.0,self.myText)
    manualWidget.pack(expand = 1, fill= BOTH)
    label_1=Label(manual,text="Word",fg="green")
    label_2=Label(manual,text="Category",fg="green")
    self.entry_1=Entry(manual)
    self.entry_2=Entry(manual)
    label_1.place(x = 200, y = 900)
    label_2.place(x = 200, y = 925)
    self.entry_1.place(x = 300, y = 900)
    self.entry_2.place(x = 300, y = 925)
    self.manual_array=set()
    self.entry_3=Entry(manual)
    self.entry_3.place(x = 600, y = 900)
    submit=Button(manual,text="Submit",bg="red",command=self.submit)
    submit.place(x = 250, y = 950)
    done=Button(manual,text="Done",bg="red",command=partial(self.done,manual))
    done.place(x = 900, y = 925)
    highlight=Button(manual,text="HIGHLIGHT",bg="red",command=partial(self.getText,manualWidget))
    highlight.place(x = 600, y = 925)
    #manual.mainloop()
  else:
    content = "Please Select a File"
    messagebox.showinfo("Error! Oops",content)


 def getText(self,manualWidget):
  text=self.entry_3.get()
  self.highlight(text,manualWidget,"yellow",0)


 def highlight(self,text,widget,color,cond): #pass cond=1 if you want to recursively highlight a set of words from the text,else pass cond=0
  try:
    search = " " + text + " "
    start=1.0
    first=widget.search(search,1.0,stopindex=END)
    widget.tag_configure("COLOR", background=color)
    if(cond==0):
     widget.tag_remove("COLOR", 1.0, "end")
    while first:
     row,col=first.split('.')
     col = int(col) + 1
     first = row+'.'+str(col)
     last=int(col)+len(search) - 2
     last=row+'.'+str(last)
     row,col=last.split('.') 
     print(first)
     print(last)
     widget.tag_add("COLOR", first,last)
     start=last
     first=widget.search(search,start,stopindex=END)
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
 
 
 def done(self,widget):
  widget.destroy()

    
 def getManual(self):
  if hasattr(self,'name'):
    manualAnnot=Toplevel() 
    manualAnnot.title("Manual Annotate: "+self.name)
    self.icon(manualAnnot)
    manualFile=open(self.name + "_manualAnnot.txt","r+")
    manualText=manualFile.read()
    manualAnnotWidget=Text(manualAnnot)
    manualAnnotWidget.insert(0.0,manualText)
    manualAnnotWidget.pack(expand = 1, fill= BOTH)
    #manualAnnot.mainloop()
  else:
    content = "Please Select a File"
    messagebox.showinfo("Error! Oops",content)


 def icon(self,window):
  icon = tkinter.Image("photo", file="/home/"+getpass.getuser()+"/TextMiner/Data/icon.png")
  window.tk.call('wm','iconphoto',window._w,icon)



mainWindow=gui()


