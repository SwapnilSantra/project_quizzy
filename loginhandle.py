import sqlite3
from PyQt5.QtWidgets import QMainWindow

class loginHandle(QMainWindow):
    def __init__(self,username,password,role):
        super(loginHandle,self).__init__()
        self.password = str(password).strip()
        self.role = str(role).strip()
        self.username = str(username).strip()
        
    def validate(self): 
        try:
            with sqlite3.connect('databases/quizzyuser.db') as logincred:
                credcheck = logincred.cursor()
                credcheck.execute("SELECT PASSWORD,ROLE FROM usersignin WHERE USERNAME = ?",(self.username,))
                
                all_row = credcheck.fetchall()
                
                for row in all_row:
                    fetched_pass,fetched_role = row

                    if fetched_pass != self.password:
                        print("Password Missmatch")
                        return 1;
                    elif fetched_role != self.role:
                        print("ROle missmatch")
                        return 2
                    print("Login Successfull")
                    return 0
        except sqlite3.Error as e:
            print("DB Error:",e)
            return -1
        except ValueError as e:
            print("Unpack Error:",e,"Check Table columns")
            return -1



