import random


def show_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even(n):
    return n % 2 == 0


def generate_question():
    number = random.randint(1, 100)
    if is_even(number):
        right_answer = 'yes'
    elif not is_even(number):
        right_answer = 'no'
    print(f'Question: {number}')
    return right_answer
