from random import randint

container = {'a': [], 'b': [], 'c': [], 'd': []}


def func(container):

    listc, listd = [], []

    for i in range(4):
        listc.append(randint(1, 40))

    for i in range(7):
        listd.append(randint(1, 40))

    for key in container.keys():
        if key == 'a':
            container[key].append(randint(1, 40))
        elif key == 'b':
            container[key].append(randint(1, 40))
        elif key == 'c':
            container[key] = listc
        elif key == 'd':
            container[key] = listd

    multiply = 1
    for key, value in container.items():
        for item in value:
            multiply *= item

    return 'd', multiply



result = func(container)
print('key - {first} \nmultiply - {second}'.format(first=result[0], second=result[1]))