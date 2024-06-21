import random


def show_rules():
    print('Find the greatest common divisor of given numbers.')


def find_gcd(number1, number2):
    while number1 != number2:
        if number1 > number2:
            number1 = number1 - number2
        else:
            number2 = number2 - number1
    return min(number1, number2)


def generate_question():
    number1 = random.randint(10, 100)
    number2 = random.randint(10, 100)
    right_answer = find_gcd(number1, number2)
    print(f'Question: {number1} {number2}')
    return right_answer
