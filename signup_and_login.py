from PyQt5.uic import loadUi
from createdb import Dblog
from PyQt5.QtWidgets import QDialog, QLineEdit
#from PyQt5 import QtWidgets
from resources.logo import *
from maindashboard import AdminDash,UserDash
from loginhandle import loginHandle
class SignUp(QDialog):
    def __init__(self,widget):
        super(SignUp,self).__init__()
        loadUi('uifiles/signup.ui',self)
        self.widget = widget
        self.signup_button.clicked.connect(self.signup_function)
        self.show_pass.clicked.connect(self.toggle_echo_mode)
        self.show_conf_pass.clicked.connect(self.toggle_echo_mode_conf)
        self.backbutton.clicked.connect(self.back)
    def signup_function(self):        
        name = self.name.text()
        role = self.role.currentText()
        username = self.username.text()
        password = self.password.text()
        conf_password = self.conf_password.text()
        if password!=conf_password:
            self.pass_warning.setText("Password not matching! Check the password while typing.")
            self.password.clear()
            self.conf_password.clear()
        else:
            if username and password:
                if name:
                    Dblog(name,username,password,role)
                    if role=="Admin":
                        print("Successfully signed as an admin")
                    if role=="User":
                        print("Successfully signed as an user")
                    self.name.clear()
                    self.username.clear()
                    self.password.clear()
                    self.conf_password.clear()
                    self.captcha_fill.clear()
                self.widget.setCurrentIndex(0)
                self.widget.setFixedHeight(665)
                self.widget.setFixedWidth(571)
            else:
                if not name:
                    self.name_warning.setText("Enter your Name")
                if not username:
                    self.usrname_warning.setText("Enter your Username")
                if not password:
                    self.pass_warning.setText("Enter your Password")

    def toggle_echo_mode(self):
        if self.password.echoMode() == QLineEdit.Password:
            self.password.setEchoMode(QLineEdit.Normal)
        else:
            self.password.setEchoMode(QLineEdit.Password)


    def toggle_echo_mode_conf(self):
        if self.conf_password.echoMode() == QLineEdit.Password:
            self.conf_password.setEchoMode(QLineEdit.Normal)
        else:
            self.conf_password.setEchoMode(QLineEdit.Password)

    def back(self):
        self.widget.setCurrentIndex(0)
        self.widget.setFixedWidth(617)
        self.widget.setFixedHeight(420)

####################################################
####################################################
class BaseLogin(QDialog):
    def __init__(self,role,ui_file,widget):
        super(BaseLogin,self).__init__()
        loadUi(ui_file,self)
        self.widget = widget
        self.role = role
        self.loginbutton.clicked.connect(self.loginfunction)
        self.signup_button.clicked.connect(self.open_signup)
        self.show_pass.clicked.connect(self.toggle_echo_mode)
        self.backbutton.clicked.connect(self.back)
    def loginfunction(self):
        username = self.username.text()
        password = self.password.text()
        role = self.role
        result = loginHandle(username,password,role)
        erroR = result.validate()    
        if erroR == 0:
            print("Successfully logined as an",role,username,password)
            while self.widget.count() > 0:
                w = self.widget.widget(0)
                self.widget.removeWidget(w)
                w.deleteLater()
            self.widget.close()
            if role == "Admin":
                self.dashboardpage = AdminDash()
                self.dashboardpage.showMaximized()
                self.close()
            if role == "User":
                self.dashboardpage = UserDash()
                self.dashboardpage.showMaximized()
                self.close()


        elif erroR == 1:
            print("Password is not correct")
        elif erroR == 2:
            print("You are not"+role+"!")
        elif erroR == -1:
            print("Username not FOund")
        elif erroR == 0:
            print("Successfully logged in..")
        else:
            print("UNknown Error,Try Again Later...")

    
    def open_signup(self):
        self.widget.setFixedHeight(685)
        self.widget.setFixedWidth(577)
        self.widget.setCurrentIndex(1)

        
    def toggle_echo_mode(self):
        if self.password.echoMode() == QLineEdit.Password:
            self.password.setEchoMode(QLineEdit.Normal)
        else:
            self.password.setEchoMode(QLineEdit.Password)
    
    def back(self):
        self.widget.setFixedHeight(420)
        self.widget.setFixedWidth(617)
        self.widget.setCurrentIndex(0)

class Adminlogin(BaseLogin):
    def __init__(self,widget):
        super().__init__("Admin","uifiles/adminlogin.ui",widget)

class Userlogin(BaseLogin):
    def __init__(self,widget):
       super().__init__("User","uifiles/userlogin.ui",widget)
