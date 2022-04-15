def is_continuous_sequence(source):
    if len(source) < 2:
        return False
    for x, y in zip(source, source[1:]):
        if (y - x) != 1:
            return False
    return True

print(is_continuous_sequence([10, 11, 12, 13])) # True
print(is_continuous_sequence([-5, -4, -3])) # True
print(is_continuous_sequence([10, 11, 12, 14, 15])) # False
print(is_continuous_sequence([1, 2, 2, 3])) # False
print(is_continuous_sequence([7])) # False
print(is_continuous_sequence([])) # False