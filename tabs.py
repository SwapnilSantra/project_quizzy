from PyQt5.uic import loadUi
from resources.logo import *
from PyQt5.QtWidgets import QDialog
class ResultWidget(QDialog):
    def __init__(self,score,total):
        super(ResultWidget,self).__init__()
        loadUi('uifiles/result.ui',self)
        self.score.setText(str(score))
        self.total.setText(str(total))
        percentage = (score/total*100) if total > 0 else 0
        self.percentage.setText(str(percentage))


class DifficultyDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('uifiles/choosedifficulty.ui',self)
        self.setWindowTitle("🎯 Select Quiz Difficulty")
        self.startbutton.clicked.connect(self.accept) 
        self.setModal(True)
        self.setFixedSize(400, 350)

    def get_difficulty(self):
        """Return selected difficulty based on radio buttons"""
        if self.easybutton.isChecked():     
            return "easy"
        elif self.mediumbutton.isChecked():
            return "medium"
        elif self.hardbutton.isChecked():
            return "hard"
        else:
            return "medium"  
