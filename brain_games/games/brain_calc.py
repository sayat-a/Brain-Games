import random


def show_rules():
    print('What is the result of the expression?')


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
    print(f'Question: {number1} {operator} {number2}')
    return right_answer
