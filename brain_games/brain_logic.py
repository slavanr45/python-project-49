import random
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    logic(name)


def logic(name):
    counter_games = 0
    while True:
        num = random.randint(1, 100)
        print('Answer "yes" if the number is even, otherwise answer "no".')
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        num = 'yes' if num % 2 == 0 else 'no'
        if answer != num:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{num}'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
            counter_games += 1
        if counter_games == 3:
            print(f'Congratulations, {name}!')
            break
