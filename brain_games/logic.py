import random
import prompt


def welcome_user(number_of_game):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    game_logic(name, number_of_game)


def game_logic(name, number_of_game):
    counter_games = 0
    while counter_games < 3:
        match number_of_game:
            case 1:
                answer, res = brain_even()
            case 2:
                answer, res = brain_calc()
        if answer != res:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{res}'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
            counter_games += 1
    else:
        print(f'Congratulations, {name}!')


def brain_even():
    num = random.randint(1, 100)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print(f'Question: {num}')
    even_answer = prompt.string('Your answer: ')
    even_result = ('no', 'yes')[num % 2 == 0]
    return even_answer, even_result


def brain_calc():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation = random.choice('+-*')
    print('What is the result of the expression?')
    print(f'Question: {num1} {operation} {num2}')
    calc_answer = prompt.integer('Your answer: ')
    calc_result = eval(f'{num1} {operation} {num2}')
    return calc_answer, calc_result
