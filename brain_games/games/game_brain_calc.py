import random
from . import game_logic


def calculate_answer(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    return result


def play_brain_calc():
    user_name = game_logic.greet_user()
    print('What is the result of the expression?')
    count_right = 0
    while count_right < 3:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        operator = random.choice(['+', '-', '*'])
        right_answer = calculate_answer(number1, number2, operator)
        print(f'Question: {number1} {operator} {number2}')
        answer = game_logic.ask_user_answer()
        if int(answer) == right_answer:
            count_right = game_logic.win_round(count_right)
        else:
            game_logic.lose_round(answer, right_answer, user_name)
            break
    if count_right == 3:
        game_logic.congratulate(user_name)
