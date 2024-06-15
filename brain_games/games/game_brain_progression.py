import prompt
import random


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
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('What number is missing in the progression?')
    count_right = 0
    while count_right < 3:
        progression, right_answer = generate_progression()
        string = ' '.join(progression)
        print(f'Question: {string}')
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
