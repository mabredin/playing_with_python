def length_of_last_word(string):
    count = 0
    end = len(string) - 1
    while string:
        while count == 0 and string[end] == ' ':
            end -= 1
        while (string[end] not in '\t\n ') and (0 <= end): # { '\t', '\n', ' ' }
            count += 1
            end -= 1
        return count
    return 0


print(length_of_last_word(''))  # 0
print(length_of_last_word('man in Black'))  # 5
print(length_of_last_word('hello, world!     '))  # 6
print(length_of_last_word('hello\t\nworld'))  # 5
print(length_of_last_word('hi'))  # 2