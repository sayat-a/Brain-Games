import prompt
import random


def calculate_answer(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    return result


def play_brain_calc():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('What is the result of the expression?')
    count_right = 0
    while count_right < 3:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        operator = random.choice(['+', '-', '*'])
        right_answer = calculate_answer(number1, number2, operator)
        print(f'Question: {number1} {operator} {number2}')
        answer = prompt.string('Your answer: ')
        if int(answer) == right_answer:
            count_right += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
    if count_right == 3:
        print(f'Congratulations, {user_name}!')
