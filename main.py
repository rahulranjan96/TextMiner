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
  self.ip="127.0.0.1"
  self.maindisplay()
  

 def maindisplay(self):
  root = Tk()
  root.minsize(1000,700)
  root.resizable(width=False, height=False)
  im = Image.open("/home/"+getpass.getuser()+"/TextMiner/Data/background.jpg")
  tkimage = ImageTk.PhotoImage(im)
  myvar=Label(root,image = tkimage)
  myvar.place(x=0, y=0, relwidth=1.0, relheight=1.0)
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
  self.var  = StringVar(root)
  self.var.set("NLTK")
  option = OptionMenu(root, self.var, "NLTK","POLYGLOT")
  option.config(width=30,height=3)
  option.place(x = 350, y = 550)
  root.mainloop()


 

 def browseButton(self,root):
  browseButton = Button(root,text="Browse",width=21,bg="red",font=self.customFont,command=partial(self.browse,root))
  browseButton.place(x = 350, y = 150)

 
 def stButton(self,root):
  stButton=Button(root,text="Sentence Tokenizer",width=21,bg="red",font=self.customFont,command=self.sentTokenizechecker)
  stButton.place(x = 350, y = 200)

 
 def wtButton(self,root):
  wtButton=Button(root,text="Word Tokenizer",width=21,bg="red",font=self.customFont,command=self.wordTokenizechecker)
  wtButton.place(x = 350, y = 250)


 def posButton(self,root):
  posButton=Button(root,text="POS Tagger",width=21,bg="red",font=self.customFont,command=self.partofSpeechchecker)
  posButton.place(x = 350, y = 300)


 def neButton(self,root):
  neButton=Button(root,text="Named Entity Recognizer",width=21,bg="red",font=self.customFont,command=self.namedEntitychecker)
  neButton.place(x = 350, y = 350)


 def manualButton(self,root):
  manualButton=Button(root,text="Manually Annotate",width=21,bg="red",font=self.customFont,command=self.manual)
  manualButton.place(x = 350, y = 400)


 def getManualButton(self,root):
  getManualButton=Button(root,text="Get Manual Annotations",width=21,bg="red",font=self.customFont,command=self.getManual)
  getManualButton.place(x = 350, y = 450)


 def dictionaryButton(self,root):
  dictionaryButton = Button(root,text="Give Dictionary",width=21,bg="red",font=self.customFont,command=self.dictionary)
  dictionaryButton.place(x = 350, y = 500)



 def sentTokenizechecker(self):
  if hasattr(self, "name"):
   if(self.var.get()=="NLTK"):
     self.sentTokenizeNLTK()
     #print("NLTK")
   else:
     #print("POLYGLOT")
     self.sentTokenizePolyglot()
  else:
   content = "Please Select a File"
   messagebox.showinfo("Error! Oops",content)


 def wordTokenizechecker(self):
  if hasattr(self, "name"):
   if(self.var.get()=="NLTK"):
     self.wordTokenizeNLTK()
     #print("NLTK")
   else:
     #print("POLYGLOT")
     self.wordTokenizePolyglot()
  else:
   content = "Please Select a File"
   messagebox.showinfo("Error! Oops",content)


 def partofSpeechchecker(self):
  if hasattr(self, "name"):
   if(self.var.get()=="NLTK"):
     self.partofSpeechNLTK()
     #print("NLTK")
   else:
     #print("POLYGLOT")
     self.partofSpeechPolyglot()
  else:
   content = "Please Select a File"
   messagebox.showinfo("Error! Oops",content)



 def namedEntitychecker(self):
  if hasattr(self, "name"):
   if(self.var.get()=="NLTK"):
     self.namedEntityNLTK()
     #print("NLTK")
   else:
     #print("POLYGLOT")
     self.namedEntityPolyglot()
  else:
   content = "Please Select a File"
   messagebox.showinfo("Error! Oops",content)
 

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
  #print(string)
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


 """def ok(self):
  vare = self.var
  a = vare.get()
  if(a=="NLTK"):
    print(a)
    self.value=0
  elif(a=="POLYGLOT"):
    print(a)
    self.value=1
  else:
    print("NLP")
  print(self.value)"""


 def docview(self,filename,root):
  docview = Toplevel() 
  docview.title("Document: "+self.name)
  self.icon(docview)
  f=open(filename,"r+")
  data = f.read()
  self.myText=data
  S = Scrollbar(docview)
  T = Text(docview,height=20)
  S.pack(side=RIGHT,fill=Y)
  T.pack(expand = 1, fill= BOTH)
  S.config(command=T.yview)
  T.config(yscrollcommand=S.set)
  T.insert(END,data)
  T.config(state=DISABLED)
  var=StringVar(docview)
  var.set("Organisation")
  option = OptionMenu(docview,var,"Organisation","Person","Location","Date","Time","Money","Percent","Facility","GPE")
  option.config(width=8,height=2)
  option.pack(side=LEFT)
  selectCategoryButton = Button(docview,text="OK",bg="red",command=partial(self.highlightchoice,var,T))
  selectCategoryButton.pack(side=LEFT)
  highlighDictionaryButton =Button(docview,text="Highlight Dictionary",bg="red",command=partial(self.highlightDictionary,T))
  highlighDictionaryButton.pack(side=RIGHT)
  #docview.mainloop()

 def highlightchoice(self,var,widget):
  choice = var.get()
  self.highlightChoiceFromDatabase(widget,choice)
  
  


 def highlightChoiceFromDatabase(self,widget,choice):
  #ip = socket.gethostbyname(self.gethostbyname())
  #if you want to connect to local database then in the place of 10.11.12.25 write ip
  #for Main Server Ip write the ip in the place of 10.11.12.25
  widget.tag_remove("COLOR", 1.0, "end")
  db = self.databaseConnection()
  cursor = db.cursor()
  table=self.name
  sql = """SELECT word FROM %s WHERE category = '%s'""" % (table,choice) 
  cursor.execute(sql)
  results = cursor.fetchall()
  for row in results:
    name = row[0]
    self.highlight(name,widget,"yellow",1)
  db.commit()
  db.close()


 
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
    name = self.name
    manual.title("Manually Annotate: "+self.name)
    self.icon(manual)
    manual.minsize(1200,600)
    manual.resizable(width=False, height=False)
    frame1=Frame(manual,width=1200,height=800)
    frame1.pack_propagate(0)
    frame2=Frame(manual,width=1200,height=200)
    frame2.pack_propagate(0)
    frame1.pack(side=TOP)
    frame2.pack(side=BOTTOM)
    S = Scrollbar(frame1)
    T = Text(frame1,height=20)
    S.pack(side=RIGHT,fill=Y)
    T.pack(expand = 1, fill= BOTH)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    T.insert(0.0,self.myText)
    T.config(state=DISABLED)
    #label_1=Label(frame2,text="Word",fg="red")
    #label_2=Label(frame2,text="Category",fg="red")
    #self.entry_1=Entry(frame2)
    #self.entry_2=Entry(frame2)
    self.submitCat=StringVar(frame2)
    self.submitCat.set("Organisation")
    option = OptionMenu(frame2,self.submitCat,"Organisation","Person","Location","Date","Time","Money","Percent","Facility","GPE")
    option.config(width=8,height=2)
    option.place(x=100,y=20)
    #label_1.place(x=100,y=50)
    #label_2.place(x=100,y=50)
    #self.entry_1.place(x=250,y=50)
    #self.entry_2.place(x=250,y=70)
    #self.manual_array=set()
    self.entry_3=Entry(frame2)
    self.entry_3.place(x=500,y=50)
    submit=Button(frame2,text="Submit",bg="red",command=partial(self.submit,T))
    submit.place(x=250,y=30)
    done=Button(frame2,text="Done",bg="red",command=partial(self.done,manual))
    done.place(x=900,y=60)
    highlight=Button(frame2,text="HIGHLIGHT",bg="red",command=partial(self.getText,T))
    highlight.place(x=500,y=100)
    #manual.mainloop()
  else:
    content = "Please Select a File"
    messagebox.showinfo("Error! Oops",content)


 def getText(self,manualWidget):
  text=self.entry_3.get()
  self.highlight(text,manualWidget,"yellow",0)


 def highlight(self,text,widget,color,cond): #pass cond=1 if you want to recursively highlight a set of words from the text,else pass cond=0
  try:
    search = text
    start=1.0
    first=widget.search(search,1.0,stopindex=END)
    widget.tag_configure("COLOR", background=color)
    if(cond==0):
     widget.tag_remove("COLOR", 1.0, "end")
    while first:
     row,col=first.split('.')
     col = int(col)
     first = row+'.'+str(col)
     last=int(col)+len(search) - 1
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




 """Method to insert manual annotations in the databse.For different files we have different tables which dynamically get created once annotation is being done."""

 def submit(self,T):
  #print(self.entry_1.get())
  #print(self.entry_2.get())
  #print(T.selection_get())
  db = self.databaseConnection()
  cursor = db.cursor()
  sql1 = """SHOW TABLES LIKE '%s'""" % self.name
  cursor.execute(sql1)
  result = cursor.fetchone()
  if result:
   word = T.selection_get()
   index_start=T.count("1.0", "sel.first")[0]
   index_end=len(word) + int(index_start)
   category = self.submitCat.get() 
   sql2 = """INSERT INTO %s (word,category,start_index,end_index) VALUES ('%s','%s','%s','%s')""" % (self.name,word,category,str(index_start),str(index_end))
   cursor.execute(sql2)
   db.commit()
  else:
   sql2 =  """CREATE TABLE %s (
       `id` INT NOT NULL AUTO_INCREMENT,
       `word` VARCHAR(50) NULL DEFAULT '',
       `category` VARCHAR(50) NULL DEFAULT '',
       `start_index` VARCHAR(50) NULL DEFAULT '',
       `end_index` VARCHAR(50) NULL DEFAULT '',
       PRIMARY KEY (id))COLLATE='utf8_bin'""" % self.name
   cursor.execute(sql2)
   word = T.selection_get()
   index_start=T.count("1.0", "sel.first")[0]
   index_end=len(word) + int(index_start)
   category = self.submitCat.get()
   sql3 = """INSERT INTO %s (word,category,start_index,end_index) VALUES ('%s','%s','%s','%s')""" % (self.name,word,category,str(index_start),str(index_end))
   cursor.execute(sql3)
   db.commit()
  db.close()


 
 
 """Method to close Manually Annotate Window"""

 def done(self,widget):
  widget.destroy()

   



 """Method to get the list of manual annotations done by users over a particular document from the central database."""

 def getManual(self):
  if hasattr(self,'name'):
    manualAnnot=Toplevel()
    filename = self.name
    manualAnnot.title("Manual Annotate: "+self.name)
    self.icon(manualAnnot)
    db = self.databaseConnection()
    cursor = db.cursor()
    sql = """SELECT * FROM %s""" % self.name
    cursor.execute(sql)
    string = ""
    results = cursor.fetchall()
    string = string + "Word" + "\t\t\t" + "Category" + "\n"
    string = string + "------------------------------------" + "\n"
    for row in results:
    	a = row[0]
    	string = string + row[1] + "\t\t\t"+ row[2] + "\n"
    db.commit()
	#manualFile=open(self.name + "_manualAnnot.txt","r+")
    #manualText=manualFile.read()
    manualText = string
    manualAnnotWidget=Text(manualAnnot)
    manualAnnotWidget.insert(0.0,manualText)
    manualAnnotWidget.pack(expand = 1, fill= BOTH)
    #manualAnnot.mainloop()
  else:
    content = "Please Select a File"
    messagebox.showinfo("Error! Oops",content)




 """Method to set icon for every new window that opens."""

 def icon(self,window):
  icon = tkinter.Image("photo", file="/home/"+getpass.getuser()+"/TextMiner/Data/icon.png")
  window.tk.call('wm','iconphoto',window._w,icon)




 """Method to connect with the application with central server to do database queries."""

 def databaseConnection(self):
  database=MySQLdb.connect(host=self.ip,user="root",passwd="",db="TextMiner",unix_socket="/opt/lampp/var/mysql/mysql.sock")
  return database





mainWindow=gui()


