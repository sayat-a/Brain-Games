import random
from . import logic


def find_gcd(number1, number2):
    while number1 != number2:
        if number1 > number2:
            number1 = number1 - number2
        else:
            number2 = number2 - number1
    return min(number1, number2)


def play_brain_gcd():
    user_name = logic.greet_user()
    print('Find the greatest common divisor of given numbers.')
    count_right = 0
    while count_right < 3:
        number1 = random.randint(10, 100)
        number2 = random.randint(10, 100)
        right_answer = find_gcd(number1, number2)
        print(f'Question: {number1} {number2}')
        answer = logic.ask_user_answer()
        if int(answer) == right_answer:
            count_right = logic.win_round(count_right)
        else:
            logic.lose_round(answer, right_answer, user_name)
            break
    if count_right == 3:
        logic.congratulate(user_name)
