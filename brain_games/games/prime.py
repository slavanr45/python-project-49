import random
import prompt


def game():
    num = random.randint(2, 20)
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    print(f'Question: {num}')
    answer = prompt.string('Your answer: ')
    result = ('no', 'yes')[num in (2, 3, 5, 7, 11, 13, 17, 19)]
    return answer, result
