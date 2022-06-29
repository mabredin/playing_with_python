from random import randint


def Generator(quantity, min, max):
    while quantity > 0:
        yield randint(min, max)
        quantity -= 1


a = Generator(10, 0, 50)
for item in a:
    print(item, end='  ')
