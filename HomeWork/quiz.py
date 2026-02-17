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
    
    def is_valid_answer(self, answer, question):
        try:
            answer = int(answer)
        except ValueError:
            print("ОШИБКА: Нужно ввести число!")
            return False
        
        if answer < 0 or answer >= len(question['options']):
            print(f"ОШИБКА: Введите число от 0 до {len(question['options']) - 1}")
            return False
        
        return True
    
    def play(self):
        print("___ ДОБРО ПОЖАЛОВАТЬ В ВИКТОРИНУ! ___")
        print("Для ответа вводите номер варианта (0, 1, 2 и т.д.)")
        
        while self.current_question_index < len(self.questions):
            question = self.ask_question()  # Задаем вопрос
            
            while True:
                answer = input(">> ")
                
                if self.is_valid_answer(answer, question):    # Проверяем корректность ввода
                    answer = int(answer) 
                    self.check_answer(answer)
                    break  # Выходим из цикла повторения вопроса
                else:
                    print("Попробуйте снова. Вот варианты ответа:")    # Если ввод некорректен, показываем подсказку
                    print(question['options'])
            
            if not self.next_question():
                break
        
        print(f"\n___ ВИКТОРИНА ЗАВЕРШЕНА! ___")
        print(f"Правильных ответов: {self.correct_answers}")


if __name__ == "__main__":
    quiz = Quiz()      # Создаем викторину
    quiz.play()        # Запускаем игру