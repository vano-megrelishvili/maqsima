def func(number):
    result = ''
    while number:
        result += str(number % 2)
        number //= 2

    return result[::-1]


print(func(8))

