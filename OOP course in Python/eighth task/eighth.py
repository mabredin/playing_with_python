from math import pi


class Cylinder:
    @staticmethod
    def make_area(d, h):
        circle = pi * d ** 2 / 4
        side = pi * d * h
        return round(circle * 2 + side, 2)

    def __init__(self, diameter, high):
        self.dia = diameter
        self.h = high
        self.__area = self.make_area(diameter, high)

    def __setattr__(self, attr, value):
        if attr in ['dia', 'h', '_Cylinder__area']:
            self.__dict__[attr] = value
            try:
                self.__dict__['_Cylinder__area'] = self.make_area(self.dia, self.h)
            except AttributeError:
                pass
        else:
            raise AttributeError

    def get_area(self):
        return self.__area


a = Cylinder(1, 2)
print(a.get_area())

print(a.make_area(2, 2))

print(a.get_area())

a.dia = 3
print(a.get_area())
