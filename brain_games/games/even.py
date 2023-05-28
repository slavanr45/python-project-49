import random
import prompt

def game():
    num = random.randint(1, 100)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print(f'Question: {num}')
    even_answer = prompt.string('Your answer: ')
    even_result = ('no', 'yes')[num % 2 == 0]
    return even_answer, even_result

