import random


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(n):
    return n % 2 == 0


def generate_question():
    number = random.randint(1, 100)
    if is_even(number):
        right_answer = 'yes'
    elif not is_even(number):
        right_answer = 'no'
    question = f'Question: {number}'
    return right_answer, question
