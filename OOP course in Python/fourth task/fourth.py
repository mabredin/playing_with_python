class Test:
    def __init__(self, name):
        self.name = name

    def __add__(self, second):
        return Test(name=f'{self.name} + {second.name}')


first = Test(name='First')
second = Test(name='Second')
third = first + second
print(third.name)