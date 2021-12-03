from itertools import permutations, product

def solution():
    N = int(input())
    numbers = list(map(int, input().split(' ')))
    plus, minus, multiple, division = map(int, input().split(' '))
    calculations = ['+' for _ in range(plus)]
    calculations += ['-' for _ in range(minus)]
    calculations += ['*' for _ in range(multiple)]
    calculations += ['/' for _ in range(division)]

    calculations_permutations = set(permutations(calculations))

    minimum = float("inf")
    maximum = -float("inf")

    numbers_origin = numbers[:]
    for elm in calculations_permutations:
        value = 0
        for idx in range(N-1):
            value = calculate(numbers[idx], numbers[idx+1], elm[idx])
            numbers[idx+1] = value
            numbers[idx] = numbers_origin[idx]

        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value

        numbers[-1] = numbers_origin[-1]
            
    print(maximum)
    print(minimum)

def calculate(num1, num2, cal):
    if cal == '+':
        return num1 + num2
    elif cal == '-':
        return num1 - num2
    elif cal == '*':
        return num1 * num2
    else:
        return int(num1 / num2)

solution()
