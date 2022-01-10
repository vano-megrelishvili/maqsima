example = {5: {6: 3}, 'hi': {18: 12}, 'no': {100: 'go'}, 50: {2: 20}}


def func(dictionary):
    result = []

    for i in dictionary.values():
        for j in i.values():
            result.append(j)

    return result


print(func(example))
