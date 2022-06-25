from math import ceil


class Wallpaper:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.square = self.width * self.height


class WinDoor:
    def __init__(self, x, y):
        self.square = x * y


class Room:
    def __init__(self, x, y, z):
        self.width = x
        self.lenght = y
        self.height = z
        self.wd = []

    def add_wd(self, w, h):
        self.wd.append(WinDoor(w, h))

    def work_surface(self):
        new_square = self.get_full_square()
        for i in self.wd:
            new_square -= i.square
        return new_square

    def get_full_square(self):
        square = 2 * self.height * (self.width + self.lenght)
        return round(square, 2)

    def get_count_wallpaper(self, wallpaper):
        return ceil(self.work_surface() / wallpaper.square)


r1 = Room(7, 5.4, 2.7)
print(f'\nПлощадь без учета окон и дверей: {r1.get_full_square()}')
r1.add_wd(1, 1)
r1.add_wd(1, 1)
r1.add_wd(1, 2)
print(f'Площадь с учетом окон и дверей: {r1.work_surface()}')
wp = Wallpaper(1, 5)
print(f'Площадь рулона обоев: {wp.square}')
print(f'Необходимое количество рулонов: {r1.get_count_wallpaper(wp)}')
