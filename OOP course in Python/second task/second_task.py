import time


class Person:
    def __init__(self, name, surname, skill=1):
        self.name = name
        self.surname = surname
        self.skill = skill

    def __del__(self):
        print(f'До свидания, мистер {self.surname} {self.name}')

    def get_info(self):
        return print(f'{self.surname} {self.name} уровень квалификации - {self.skill}')


first = Person('Alex', 'Petrov', 5)
second = Person('Maxim', 'Philips')
third = Person('Yan', 'Samsung', 3)

my_list = [first, second, third]
lowest_skill = 5

for item in my_list:
    item.get_info()
    if item.skill <= lowest_skill:
        obj = item
        lowest_skill = item.skill
        del item

print(f'\nСамый слабый сотрудник {obj.surname} {obj.name} (скилл {lowest_skill})\n')

time.sleep(4)
del first
del second
del third
