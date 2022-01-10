from random import randint


def func():
    tp, odd, even, threes = (), (), (), ()
    for i in range(100):
        tp += (randint(1, 100),)

    for item in tp:
        if item % 2:
            odd += (item,)
        else:
            even += (item,)

        if item % 3 == 0:
            threes += (item,)

    return even, odd, threes


with open('./task2.txt', mode='a') as file:
    tuples = func()
    file.write('\n')
    for element in tuples:
        file.write(', '.join([str(i) for i in element]) + '\n')
