
from PyQt5.QtWidgets import QDialog

from PyQt5.uic import loadUi

class Welcome(QDialog):
    def __init__(self,widget):
        super(Welcome,self).__init__()
        loadUi('uifiles/welcome.ui',self)
        self.widget = widget
        self.admin_button.clicked.connect(self.open_admin_login)
        self.user_button.clicked.connect(self.open_user_login)
        self.signup_button.clicked.connect(self.open_signup)

    def open_welcomepage(self):
       
        self.widget.setCurrentIndex(0)

    def open_admin_login(self):
        self.widget.setFixedHeight(571)
        self.widget.setFixedWidth(665) 
        self.widget.setCurrentIndex(2)

    def open_user_login(self):
        self.widget.setFixedHeight(571)
        self.widget.setFixedWidth(665)
        self.widget.setCurrentIndex(3)

    def open_signup(self):
        self.widget.setFixedHeight(550)
        self.widget.setCurrentIndex(1)
