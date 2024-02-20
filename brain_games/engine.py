from brain_games.cli import welcome_user


def start_game(name_of_game):
    name = welcome_user()
    counter_games = 0
    while counter_games < 3:
        answer, res = name_of_game.game()
        if answer != res:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{res}'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
            counter_games += 1
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    start_game(name='John Doe', number_of_game=1)
