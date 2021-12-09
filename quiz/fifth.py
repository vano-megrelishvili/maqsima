def func(binary):
    result = 0
    for ind, char in enumerate(binary):
        if char not in ['0', '1']:
            raise ValueError('input should be binary')
        result += int(char) * pow(2, ind)

    return result


try:
    print(func('1001'))
except ValueError as err:
    print(err)
