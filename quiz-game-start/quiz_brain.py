class QuizBrain:
    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = str(input(f"Q.{self.question_number + 1}: {current_question.text}. (True/False)?: "))
        self.question_number += 1
        return answer

    def check_answer(self, answer):
        if answer.lower() == self.question_list[self.question_number - 1].answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Wrong!")
        print(F"You've scored {self.score}/{self.question_number}")