import data, question_model, quiz_brain

question_bank = []
for q in data.question_data:
    q_text = q["text"]
    q_answer = q["answer"]
    question = question_model.Question(text=q_text, answer=q_answer)
    question_bank.append(question)

quiz = quiz_brain.QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()


print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.q_number}")
