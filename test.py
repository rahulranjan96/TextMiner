import MySQLdb


db=MySQLdb.connect(host="localhost",user="root",passwd="",db="TextMiner",unix_socket="/opt/lampp/var/mysql/mysql.sock")
c=db.cursor()
sql =  """CREATE TABLE prg_config (
       `id` INT NOT NULL AUTO_INCREMENT,
       `name` VARCHAR(50) NULL DEFAULT '',
       `value` VARCHAR(50) NULL DEFAULT '',
       PRIMARY KEY (id))COLLATE='utf8_bin'"""
c.execute(sql)
db.commit()