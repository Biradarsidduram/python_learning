class QuizBrain:

  def __init__(self, question_lists):
    self.question_number = 0
    self.question_lists = question_lists
    self.score = 0

  def next_question(self):
    curent_question = self.question_lists[self.question_number]
    user_answer = input("Q.{}: {} (True/False)?: ".format(self.question_number+1, curent_question.question)).lower()
    self.question_number +=1
    self.check_answer(user_answer, curent_question.correct_answer.lower())

  def check_answer(self, user_answer, correct_answer):
    if user_answer == correct_answer:
      print("You got it right!")
      self.score +=1
    else:
      print("You got it wrong!") 
    print(f"The correct answer was: {correct_answer}")
    print(f"You current is: {self.score}/{self.question_number}")
       

  def still_has_question(self):
    if len(self.question_lists) == self.question_number:
      return False
    return True