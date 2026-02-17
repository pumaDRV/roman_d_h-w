class Quiz:
    def __init__(self):
        self.questions = [
            {
                'index': 0,
                'question': 'Столица России?',
                'options': ['Москва', 'Питер', 'Новгород'],
                'correct': 0  #ответ: Москва
            },
            {
                'index': 1,
                'question': 'Сколько ног у паука?',
                'options': ['6', '8', '10'],
                'correct': 1  #ответ: 8
            },
            {
                'index': 2,
                'question': 'Сколько планет в солнечной системе?',
                'options': ['8', '9', '7'],
                'correct': 0  #ответ: 8
            }
        ]
        self.current_question_index = 0  # Индекс текущего вопроса
        self.correct_answers = 0  # Счетчик правильных ответов
    
    def ask_question(self):
        question = self.questions[self.current_question_index]
        print(f"\n{question['question']}")
        print(question['options'])  # Выводим список вариантов
        return question
    
    def check_answer(self, answer_index):
        question = self.questions[self.current_question_index]
        if answer_index == question['correct']:
            print("Верно!")
            self.correct_answers += 1
            return True
        else:
            print("Неверно!")
            return False
    
    def next_question(self):
        self.current_question_index += 1
        return self.current_question_index < len(self.questions)
    
    def play(self):
        print("___ ДОБРО ПОЖАЛОВАТЬ В ВИКТОРИНУ! ___")
        
        while self.current_question_index < len(self.questions):
            self.ask_question()  # Задаем вопрос

            try:       # Получаем ответ 
                answer = int(input(">> "))  
                self.check_answer(answer)   # Проверка ответа
            except ValueError:
                print("Пожалуйста, введите номер ответа (число)")
                continue  # к началу цикла
            
            # Переходим к следующему вопросу
            # Если вопросы закончились, выходим из цикла
            if not self.next_question():
                break
        
        print(f"\n___ ВИКТОРИНА ЗАВЕРШЕНА! ___")
        print(f"Правильных ответов: {self.correct_answers}")


if __name__ == "__main__":
    quiz = Quiz()      # Создаемвикторину
    quiz.play()        # Запускаем игру