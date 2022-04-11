import random


class Warrior:
    health = 100

    def __init__(self, name):
        self.name = name

    def hit(self, obj):
        obj.was_hit()
        self.hit_message(obj)
        obj.health_message()
        self.health_check(obj)

    def was_hit(self):
        self.health = self.health - 20

    def hit_message(self, obj):
        print(f'{self.name} ударил {obj.name}')

    def health_message(self):
        print(f'{self.name} имеет {self.health} очков жизни\n')

    def health_check(self, obj):
        if obj.health == 0:
            print(f'{self.name} одержал победу над {obj.name}')
            return exit()

# Create instances of the Warrior class
first = Warrior(name='First')
second = Warrior(name='Second')

first.health_message()
second.health_message()

# Identifying a winner using random.sample()
list_warriors = [first, second]

while True:
    one, two = random.sample(list_warriors, 2)
    one.hit(two)
