#########Imports###################################################
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from Welcomepage import Welcome
from signup_and_login import SignUp,Adminlogin,Userlogin
###################################################################
###################################################################
###################################################################
###################################################################
####################Main function##################################


if __name__ == "__main__":

    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    mainwindow = Welcome(widget)
    signup_window = SignUp(widget)
    adminlogin_window = Adminlogin(widget)
    userlogin_window = Userlogin(widget)
    widget.addWidget(mainwindow)    #0 ... Main Window 
    widget.addWidget(signup_window) #1 ... signup Window
    widget.addWidget(adminlogin_window) #2 ... Main Login Window
    widget.addWidget(userlogin_window) #3 ... User Login Window
    widget.setCurrentIndex(0)

    widget.setFixedWidth(661)
    widget.setFixedHeight(482)
    widget.show()
    app.exec_()
