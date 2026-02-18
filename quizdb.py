import sqlite3

class QuizLoader:
    def __init__(self, db_path='databases/quiz.db'):
        self.db_path = db_path
        self.quiz_data = []
        self.question_ids = []

        self.TABLES ={
            'easy':'easy_questions',
            'medium':'medium_questions',
            'hard':'hard_questions'
        }
    
    def load_quiz_data(self,difficulty = "medium"):
        """Load all questions from database"""
        table_name = self.TABLES.get(difficulty,self.TABLES['medium'])
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f"""SELECT QID,QUESTION,OPTION1,OPTION2,OPTION3,OPTION4 FROM {table_name} ORDER BY RANDOM() LIMIT 20""")
        self.quiz_data = cursor.fetchall()
        self.question_ids = [row[0] for row in self.quiz_data]
        conn.close()
        print(f"Loaded {len(self.quiz_data)} questions")
        return self.quiz_data
    
    def get_question(self, index):
        """Get question data by index"""
        if 0 <= index < len(self.quiz_data):
            qid, question, op1, op2, op3, op4 = self.quiz_data[index]
            return {
                'id': qid,
                'question': question,
                'options': [op1, op2, op3, op4],
                'page_index': index,
            }
        return None
    def calculate_score(self,user_answer,difficulty):
        self.user_answers = user_answer
        self.difficulty = difficulty
        """Compare user answers vs correct answers from DB"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        table_name = self.TABLES.get(self.difficulty, self.TABLES['medium'])
        print(f"📊 Scoring from table: {table_name}")                            
        
        score = 0
        total = 0
                                                                 
        for qid, user_answer in self.user_answers.items():
            cursor.execute(f"SELECT CORRECTOP FROM {table_name} WHERE QID = ?", (qid,))
            result = cursor.fetchone()
                                                                                                                             
            if result:
                correct_option = result[0]  # 0=op1, 1=op2, 2=op3, 3=op4
                correct_name = f"option{correct_option + 1}"  # option1, option2..
                total += 1
                if user_answer == correct_name:
                    score += 1
                    print(f"✅ Q{qid}: Correct ({user_answer})")
                else:
                    print(f"❌ Q{qid}: Wrong ({user_answer} vs {correct_name})")
        conn.close() 
        return score, total
