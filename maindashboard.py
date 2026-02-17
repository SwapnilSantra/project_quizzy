from resources.logo import *
#from PyQt5 import QtWidgets
from PyQt5.QtCore import QPropertyAnimation,QEasingCurve, QRect
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from quizdashboard import QuizForm
class BaseDash(QMainWindow):
    def __init__(self,ui_file):
        super(BaseDash,self).__init__()
        loadUi(ui_file,self)
        
        self.leftmenu.setFixedWidth(221)
        self.leftmenu.setVisible(False)

        self.panel_animation = QPropertyAnimation(self.leftmenu,b"geometry")
        self.panel_animation.setDuration(300)
        self.panel_animation.setEasingCurve(QEasingCurve.OutCubic)

        self.togglemenu.clicked.connect(self.toggle_left_menu)
        self.toggleback.clicked.connect(self.toggle_left_menu)

        self.startquiz.clicked.connect(self.start_quiz) 
    
    def toggle_left_menu(self):
    
        if not self.leftmenu.isVisible():
            self.leftmenu.show()
            self.panel_animation.setDuration(300)
            self.panel_animation.setStartValue(QRect(-250, 0, 250, 860))  # Off left
            self.panel_animation.setEndValue(QRect(0, 0, 250, 860))        # Slide to position 0
        else:
            # SLIDE OUT to LEFT (visible → off-screen)
            self.panel_animation.setDuration(300)
            self.panel_animation.setStartValue(QRect(0, 0, 250, 860))      # Current position
            self.panel_animation.setEndValue(QRect(-250, 0, 250, 860))     # Slide off left
            self.panel_animation.finished.connect(self.hide_once)
    
        self.panel_animation.start()
        
    def hide_once(self):
        """Hide panel only after close animation finishes"""
        self.leftmenu.hide()
        self.panel_animation.finished.disconnect(self.hide_once)  # Clean up
    
    def start_quiz(self):
        self.quizpage = QuizForm()
        self.quizpage.showNormal()
        self.close()

class AdminDash(BaseDash):
   def __init__(self):
       super().__init__("uifiles/admindash.ui")

class UserDash(BaseDash):
    def __init__(self):
        super().__init__("uifiles/userdash.ui")
