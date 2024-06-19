import random
from . import logic


def is_prime(number):
    count = 0
    for i in range(1, number):
        if number % i == 0:
            count += 1
    if count == 1:
        return True
    else:
        return False


def play_brain_prime():
    user_name = logic.greet_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count_right = 0
    while count_right < 3:
        number = random.randint(2, 100)
        if is_prime(number):
            right_answer = 'yes'
        elif not is_prime(number):
            right_answer = 'no'
        print(f'Question: {number}')
        answer = logic.ask_user_answer()
        if answer == right_answer:
            count_right = logic.win_round(count_right)
        else:
            logic.lose_round(answer, right_answer, user_name)
            break
    if count_right == 3:
        logic.congratulate(user_name)
