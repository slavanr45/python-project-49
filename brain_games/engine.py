from brain_games.games import calc, even, gcd, progression, prime


def start_game(name, number_of_game):
    counter_games = 0
    while counter_games < 3:
        match number_of_game:
            case 1:
                answer, res = even.game()
            case 2:
                answer, res = calc.game()
            case 3:
                answer, res = gcd.game()
            case 4:
                answer, res = progression.game()
            case 5:
                answer, res = prime.game()
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
