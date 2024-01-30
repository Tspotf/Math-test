import random
def generate_math_question(num1,num2):
    num1=random.randint(num1,num2)
    num2 = random.randint(num1, num2)
    operater= random.choice(['-','+','/','*'])
    result=f'{num1} {operater} {num2}'
    return result
def check_answer(numbers,answer):
    try:
        answer=float(answer)
        return answer==eval(numbers)

    except ValueError:
        return False
def math_quiz(number_of_questions=5):
    print("Добро пожаловать в математический тест!")
    correct_answers = 0

    for i in range(number_of_questions):
        numbers1=generate_math_question(1,5)
        answer = input(f"{numbers1} = ")
        if check_answer(numbers1,answer):
            correct_answers += 1
    print("Тест завершен.")
    print(f"Вы правильно решили {correct_answers} из {number_of_questions} вопросов.")

    if correct_answers>=number_of_questions*0.8:
        print("Отлично! Вы получаете оценку A.")
    elif correct_answers>=number_of_questions*0.6:
        print("Хорошо! Вы получаете оценку B.")
    else:
        print("Попробуйте еще раз. Вы получаете оценку C.")
math_quiz(7)
