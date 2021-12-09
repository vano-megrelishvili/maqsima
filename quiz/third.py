s = 'hihellohellonohellon'
find = 'hello'


def func(word, find):
    count = 0
    for ind in range(len(s) - len(find) + 1):
        if word[ind:ind + len(find)] == find:
            count += 1

    return count


print(func(s, find))
