import random


class Unit:
    def __init__(self, id, team):
        self.id = id
        self.team = team


class Hero(Unit):
    def __init__(self, id, team, level=1):
        # Unit.__init__(self, id, team)
        super().__init__(id, team)
        self.level = level

    def level_up(self):
        self.level = self.level + 1


class Soldier(Unit):

    def follow_the_Hero(self, hero):
        print(f'Солдат {self.id} следует за своим героем {hero.id}')


def show_teams(team_list):
    for item in team_list:
        print(item.__dict__)


def population_check_result(hero):
    hero.level_up()
    print(f"\nВойско героя {hero.id} больше. Поэтому его уровень увеличен до {hero.level}")


# Инициализация героев и списков солдат
hero_left = Hero(1, 'Left')
hero_right = Hero(2, 'Right')
list_left = []
list_right = []

# Демострация героев
print(f'Герой команды "Left" {hero_left.__dict__}')
print(f'Герой команды "Right" {hero_right.__dict__}\n')

# Создание солдат и заполнение ими списков
for soldier in range(10):
    soldier = Soldier(soldier + 3, random.choice(['Left', 'Right']))
    if soldier.team == 'Left':
        list_left.append(soldier)
    else:
        list_right.append(soldier)

# Демонстрация команд
print(f'Команда "Left" имеет состав из {len(list_left)} участников:')
show_teams(list_left)
print(f'\nКоманда "Right" имеет состав из {len(list_right)} участников:')
show_teams(list_right)

# Проверка численности команд и увеличени еуровня нужного героя
if len(list_left) > len(list_right):
    population_check_result(hero_left)
elif len(list_left) < len(list_right):
    population_check_result(hero_right)
else:
    print('\nЧисленности команд равны. Уровень героев остается прежним!\n')

# Случайный солдат команды 1 следует за своим героем
soldier = random.choice(list_left)
soldier.follow_the_Hero(hero_left)
