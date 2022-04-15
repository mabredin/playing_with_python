from collections import Counter


def scrabble(string, word):
    dict_c = dict(Counter(string.casefold()).most_common())
    dict_d = dict(Counter(word.casefold()).most_common())
    if dict_c.keys() & dict_d.keys() == dict_d.keys():
        for key in dict_d:
            if dict_d[key] > dict_c[key]:
                return False
        return True
    return False


print(scrabble('rkqodlw', 'world')) # True
print(scrabble('avj', 'java')) # False
print(scrabble('avjafff', 'java')) # True
print(scrabble('', 'hexlet')) # False
print(scrabble('scriptingjava', 'JavaScript')) # True