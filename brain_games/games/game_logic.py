import prompt


def greet_user():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def ask_user_answer():
    answer = prompt.string('Your answer: ')
    return answer


def win_round(count):
    print('Correct!')
    return count + 1


def lose_round(wrong, right, name):
    print(f"'{wrong}' is wrong answer ;(. Correct answer was '{right}'.")
    print(f"Let's try again, {name}!")


def congratulate(name):
    print(f'Congratulations, {name}!')
