def is_degenerated(line):
    if (line[0][0] == line[1][0]) | (line[0][1] == line[1][1]):
        if (line[0][0] + line[1][0] != 0) & (line[0][1] + line[1][1] != 0):
            return True
    return False


def is_vertical(line):
    if (line[0][0] == line[1][0]) & (line[0][1] != line[1][1]):
        return True
    return False


def is_horizontal(line):
    if (line[0][1] == line[1][1]) & (line[0][0] != line[1][0]):
        return True
    return False


def is_inclined(line):
    if (line[0][0] != line[1][0]) & (line[0][1] != line[1][1]):
        return True
    return False

line1 = ((0, 10), (100, 130))
print(is_degenerated(line1)) # False
print(is_vertical(line1)) # False
print(is_horizontal(line1)) # False
print(is_inclined(line1)) # True

print('--------------')

line2 = ((42, 1), (42, 2))
print(is_vertical(line2)) # True

print('--------------')

line3 = ((100, 50), (200, 50))
print(is_horizontal(line3)) # True

print('--------------')

line4 = ((15, 5), (15, -5))
print(is_degenerated(line4))