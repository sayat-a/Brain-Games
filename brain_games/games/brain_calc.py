import random


GAME_RULES = 'What is the result of the expression?'


def calculate_answer(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    return result


def generate_question():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    right_answer = calculate_answer(number1, number2, operator)
    question = f'{number1} {operator} {number2}'
    return right_answer, question
