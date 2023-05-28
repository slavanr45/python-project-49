import random
import prompt


def game():
    num = random.randint(1, 100)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print(f'Question: {num}')
    answer = prompt.string('Your answer: ')
    result = ('no', 'yes')[num % 2 == 0]
    return answer, result
