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


