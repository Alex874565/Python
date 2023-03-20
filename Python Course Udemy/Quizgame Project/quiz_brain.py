class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.correct_answers = 0

    def next_question(self):
        self.question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {self.question.text} (True/False)?: ")
        return answer

    def correct_answer(self):
        print("That's correct!")
        self.correct_answers += 1
        print(f"Correct answers: {self.correct_answers}/{self.question_number}")

    def incorrect_answer(self):
        print(f"That was incorrect. The correct answer was {self.question.answer}.")

    def check_answer(self):
        return self.next_question().lower() == self.question.answer.lower()

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def run(self):
        winning = True

        while self.still_has_questions():
            
            if self.check_answer() == True:
                self.correct_answer()
            else:
                self.incorrect_answer()
                winning = False

        if winning:
            print("You won!")
        else:
            print("You lost :(")
            print(f"Correct answers: {self.correct_answers}/{len(self.question_list)}") 
