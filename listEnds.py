from random import sample
a = sample(range(100), 20)


def first_last(x):
    value = [x[0], x[-1]]
    return print(value)

first_last(a)
