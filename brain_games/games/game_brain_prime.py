import prompt
import random


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
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('Answer "yes" if given number is prime, otherwise answer "no".')
    count_right = 0
    while count_right < 3:
        number = random.randint(2, 100)
        if is_prime(number):
            right_answer = 'yes'
        elif not is_prime(number):
            right_answer = 'no'
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if answer == right_answer:
            count_right += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
    if count_right == 3:
        print(f'Congratulations, {user_name}!')
