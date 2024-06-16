import random
from . import game_logic


def is_even(n):
    return n % 2 == 0


def play_brain_even():
    user_name = game_logic.greet_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count_right = 0
    while count_right < 3:
        number = random.randint(1, 100)
        if is_even(number):
            right_answer = 'yes'
        elif not is_even(number):
            right_answer = 'no'
        print(f'Question: {number}')
        answer = game_logic.ask_user_answer()
        if answer == right_answer:
            count_right = game_logic.win_round(count_right)
        else:
            game_logic.lose_round(answer, right_answer, user_name)
            break
    if count_right == 3:
        game_logic.congratulate(user_name)
