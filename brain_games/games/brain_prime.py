import random


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    count = 0
    for i in range(1, number):
        if number % i == 0:
            count += 1
    if count == 1:
        return True
    else:
        return False


def generate_question():
    number = random.randint(2, 100)
    if is_prime(number):
        right_answer = 'yes'
    elif not is_prime(number):
        right_answer = 'no'
    question = f'Question: {number}'
    return right_answer, question
