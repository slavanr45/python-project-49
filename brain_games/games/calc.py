import random
import prompt

def game():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice('+-*')
    print('What is the result of the expression?')
    print(f'Question: {num1} {operator} {num2}')
    calc_answer = prompt.integer('Your answer: ')
    calc_result = eval(f'{num1} {operator} {num2}')
    return calc_answer, calc_result

