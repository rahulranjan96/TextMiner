[![AUR](https://img.shields.io/aur/license/yaourt.svg?maxAge=2592000?style=flat-square)](https://raw.githubusercontent.com/rahulranjan96/TextMiner/master/LICENSE.txt?token=APHqCzbjidKXSG9I056xLviUt6URhmBtks5XZ6kYwA%3D%3D)

TextMiner 1.0
==============

NLP based information extractor:
-------------------------------

#Platforms
This standalone application has been developed on Ubuntu 16.04.Ubuntu 14.04 should be workable.Windows users should install Ubuntu.

#Proxy Settings:
###Setting proxy authentication in apt.conf file:
```
$ sudo gedit /etc/apt/apt.conf
```
Add following lines in the file:
```
Acquire::http::proxy "http://username:password@proxy:port/";
Acquire::https::proxy "https://username:password@proxy:port/";
Acquire::ftp::proxy "ftp://username:password@proxy:port/";
Acquire::socks::proxy "socks://username:password@proxy:port/";

```
###Setting proxy authentication in environment file:
```
$ sudo gedit /etc/environment
```
Add following lines in the file:
```
http_proxy="http://username:password@proxy:port/"
https_proxy="https://username:password@proxy:port/"
ftp_proxy="ftp://username:password@proxy:port/"
socks_proxy="socks://username:password@proxy:port/"
```
###Setting proxy authentication in bash file:
```
$ sudo gedit ~/.bashrc

```
Add following lines at the last line of the file:
```
export {http,https,ftp}_proxy='http://username:password@proxy:port'

```

#Dependencies Installations:
At present this application is simple enough but stands on some pretty complex Python Libraries which users should install before running this application.

###This software has been written in Python3.4 and Python3.4 is required to run it.
To install Python3.4
```
$ sudo apt-get install python3

```
To install pip3 which will be further used to install other python libraries.
```
$ sudo apt-get install python3-pip

```
###We also require numpy library to do some mathematical calculations.
```
$ sudo pip3 install -U numpy
```
###For Natural Language Processing this software uses two python libraries named NLTK and Polyglot.
To install NLTK:
```
$ sudo pip3 install -U nltk
```
Then we have to download the training data for NLTK.

```
$ python3
>> import nltk
>> nltk.download()
NLTK Downloader
---------------------------------------------------------------------------
    d) Download   l) List    u) Update   c) Config   h) Help   q) Quit
---------------------------------------------------------------------------
Downloader> d

Download which package (l=list; x=cancel)?
  Identifier> all


```

To install Polyglot:
```
$ sudo pip3 install polyglot

```
Then we have to download models for Polyglot.
```
$ python3
>> from polyglot.downloader import downloader
>> downloader.download("embeddings2.en")
>> downloader.download("pos2.en")
>> downloader.download("ner2.en")
```

###We are using MySQLdb to connect MySQL database via python script.
To install MySQLdb:
```
$ sudo apt-get install python3-mysqldb


```

###We are also using Tkinter and Pillow libraries for building GUI.
To install Tkinter:
```
$ sudo apt-get install python3-tk

```
To install Pillow:
```
$ sudo pip3 install Pillow
$ sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk
$ sudo apt-get install python3-pil.imagetk OR $ sudo apt-get install python3-imaging-tk

```
#Setting up the server:

###Download and install XAMPP server for Linux.[https://www.apachefriends.org/index.html]


###To Start the XAMPP Server:
```
$ sudo /opt/lampp/lampp start

```

#To download and run this application

###Clone this reository:
```
$ git clone https://github.com/rahulranjan96/TextMiner.git
```
###To run this application:

```
$ cd TextMiner
$ python3 main.py

```
