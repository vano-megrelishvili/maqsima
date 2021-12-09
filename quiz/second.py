from random import randint


def create():
    dictionary = {'a': [], 'b': [], 'c': [], 'd': []}

    for key in dictionary.keys():
        if key == 'c':
            dictionary[key].extend([randint(1, 100) for i in range(4)])
        elif key == 'd':
            dictionary[key].extend([randint(1, 100) for i in range(7)])
        else:
            dictionary[key].append(randint(1, 100))

    return dictionary


def func(container):
    max_key, final_key,  multiply = 0, None, 1
    for key, value in container.items():
        if max_key < len(value):
            max_key = len(value)
            final_key = key
        for item in value:
            multiply *= item

    return key, multiply


result = func(create())
print(f'max key - {result[0]}\nmultiply - {result[1]}')
