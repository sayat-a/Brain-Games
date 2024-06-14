import prompt
import random


def gcd(number1, number2):
    while number1 != number2:
        if number1 > number2:
            number1 = number1 - number2
        else:
            number2 = number2 - number1
    return min(number1, number2)



def main():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('Find the greatest common divisor of given numbers.')
    count_right = 0
    while count_right < 3:
        number1 = random.randint(10, 100)
        number2 = random.randint(10, 100)
        right_answer = gcd(number1, number2)
        print(f'Question: {number1} {number2}')
        answer = prompt.string('Your answer: ')
        if int(answer) == right_answer:
            count_right += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
    if count_right == 3:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
