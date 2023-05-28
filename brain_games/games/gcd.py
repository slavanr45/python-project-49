import random
import prompt
import math


def game():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    print('Find the greatest common divisor of given numbers.')
    print(f'Question: {num1} {num2}')
    answer = prompt.integer('Your answer: ')
    result = math.gcd(num1, num2)
    return answer, result
