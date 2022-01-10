container = [5,6,2,12,3]


def fib(n):
    if n == 0:
        return 0
    elif n < 3:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def iteration(container):
    result = []
    for i in container:
        result.append(fib(i))

    return result


print(iteration(container))