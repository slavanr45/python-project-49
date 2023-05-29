import random as rd
import prompt


def game():
    start = rd.randint(1, 20)
    step = rd.randint(1, 5)
    length = rd.randint(5, 15)
    lst = list(range(start, start + step * length, step))
    i = rd.randint(0, length - 1)
    result = lst[i]
    lst[i] = '..'
    print('What number is missing in the progression?')
    print('Question: ', end='')
    print(*lst)
    answer = prompt.integer('Your answer: ')
    return answer, result
