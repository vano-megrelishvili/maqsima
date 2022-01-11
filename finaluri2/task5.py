S = 'yzabdecw'


def func(word):
    result, current = '', ''
    for i in word:
        if len(current) == 0:
            current += i
            continue
        else:
            if ord(i) > ord(current[-1]):
                current += i
            else:
                if len(current) > len(result):
                    result = current

                current = i

    return result


print(func(S))
