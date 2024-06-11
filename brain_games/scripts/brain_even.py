import prompt
import random


def is_even(n):
    return n % 2 == 0


def main():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count_right = 0
    while count_right < 3:
        number = random.randint(1, 100)
        if is_even(number):
            right_answer = 'yes'
        elif not is_even(number):
            right_answer = 'no'
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if answer == right_answer:
            count_right += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
    if count_right == 3:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
