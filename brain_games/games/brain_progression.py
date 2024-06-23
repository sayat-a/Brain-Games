import random


GAME_RULES = 'What number is missing in the progression?'


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


def generate_question():
    progression, right_answer = generate_progression()
    string = ' '.join(progression)
    question = f'Question: {string}'
    return right_answer, question
