import prompt
from brain_games.engine import start_game


def welcome_user(number_of_game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    start_game(name, number_of_game)
