from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow,QStackedWidget
import json
from PyQt5.QtWidgets import (QMainWindow,QLabel, QRadioButton)
from resources.logo import *
from quizdb import QuizLoader
from result import ResultWidget
class QuizForm(QMainWindow):
    def __init__(self):
        super(QuizForm,self).__init__()
        loadUi('uifiles/quizpage.ui',self)

        self.quiz_loader = QuizLoader()
        self.user_answer={}

        self.load_quiz()

        self.stackedWidget.setCurrentIndex(0)
    
        self.nextbutton.clicked.connect(self.nextquestion)
        self.saveandcont.clicked.connect(self.save_and_continue)
        self.finishbutton.clicked.connect(self.finish_quiz)
    def load_quiz(self):
        """Load quiz using QuizLoader"""
        self.quiz_loader.load_quiz_data()
        
        for i in range(min(self.stackedWidget.count(), len(self.quiz_loader.quiz_data))):
            question_data = self.quiz_loader.get_question(i)
            self.fill_page(i, question_data)
    def fill_page(self, page_index, question_data):
        page = self.stackedWidget.widget(page_index)
    
        question_label = page.findChild(QLabel, "questionLabel")
        radios = page.findChildren(QRadioButton)[:4]
    
        if question_label:
            question_label.setText(f"Q{page_index+1}: {question_data['question']}")
    
        for i, radio in enumerate(radios):
            if i < len(question_data['options']):
                radio.setText(question_data['options'][i])
    
        page.question_id = question_data['id']

    def get_current_page_answers(self):
        current_page = self.stackedWidget.currentWidget()
        radios = current_page.findChildren(QRadioButton)[:4]
    
        for i, radio in enumerate(radios):
            if radio.isChecked():
                return f"option{i+1}"
        return None   
    def save_and_continue(self):
        """SAVE answer + go NEXT"""
        current_idx = self.stackedWidget.currentIndex()
        qid = self.stackedWidget.widget(current_idx).question_id
        answer = self.get_current_page_answers()
        print(f"🔍 SAVE DEBUG: qid={qid}, answer={answer}")
        if answer:
            self.user_answers[qid] = answer
            print(f"Saved Q{current_idx+1}: {answer}")
        else:
            print("No answer selected")
        
        self.nextquestion()
    
    def nextquestion(self):
        """JUST go NEXT (no save)"""
        current = self.stackedWidget.currentIndex()
        total = self.stackedWidget.count()
        if current + 1 < total:
            self.stackedWidget.setCurrentIndex(current + 1)
            print(f"→ Q{current+2}/{total}")
    
    def finish_quiz(self):
        """FINALIZE + show results"""
        self.save_quiz_progress()
        score, total = self.quiz_loader.calculate_score(self.user_answer)
        self.results_widget = ResultWidget(score, total)
        self.stackedwindow = QStackedWidget()
        self.stackedwindow.addWidget(self.results_widget)
        self.stackedwindow.setCurrentIndex(0)
        self.stackedwindow.show()
    def save_quiz_progress(self):
        """Save progress to JSON"""
        progress = {
            'answers': self.user_answer,
            'current_question': self.stackedWidget.currentIndex()
        }
        with open('quiz_progress.json', 'w') as f:
            json.dump(progress, f)
        print("Progress saved!")
    
