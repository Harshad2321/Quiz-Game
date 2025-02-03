from data import question_data
from question_model import Question
from quiz_brain import QuestionBrain
questions = [Question(q["question"], q["correct_answer"]) for q in question_data]
quiz = QuestionBrain(questions)
while quiz.still_has_questions():
    quiz.next_question()
    print("\n" + "-" * 40 + "\n")  
print("🎉 You've completed the quiz! 🎉")
print(f"Your final score is: {quiz.score}/{len(questions)} 🎯")
