import sqlite3

from PyQt5.QtWidgets import QDialog
class Dblog(QDialog):
    def __init__(self,name,username,password,role):
        super(Dblog,self).__init__()
        quizzydb = sqlite3.connect('databases/quizzyuser.db')
        curlog = quizzydb.cursor()
        curlog.execute('''INSERT INTO usersignin(NAME,USERNAME,ROLE,PASSWORD) VALUES (?,?,?,?);''',(name,username,role,password))
        quizzydb.commit()
        curlog.close()



