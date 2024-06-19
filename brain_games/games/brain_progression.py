import random
from . import logic


def generate_progression():
    step = random.randint(1, 10)
    begin = random.randint(1, 100)
    progression = [begin]
    while len(progression) < 10:
        new_elem = begin + step
        progression.append(new_elem)
        begin = new_elem
    answer = random.choice(progression)
    progression[progression.index(answer)] = '..'
    progression = list(map(str, progression))
    return progression, answer


def play_brain_progression():
    user_name = logic.greet_user()
    print('What number is missing in the progression?')
    count_right = 0
    while count_right < 3:
        progression, right_answer = generate_progression()
        string = ' '.join(progression)
        print(f'Question: {string}')
        answer = logic.ask_user_answer()
        if int(answer) == right_answer:
            count_right = logic.win_round(count_right)
        else:
            logic.lose_round(answer, right_answer, user_name)
            break
    if count_right == 3:
        logic.congratulate(user_name)
