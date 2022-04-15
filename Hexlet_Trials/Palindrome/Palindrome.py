def is_palindrome(string):
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    return False


print(is_palindrome('')) # True
print(is_palindrome('radar')) # True
print(is_palindrome('a')) # True
print(is_palindrome('abs')) # False
print(is_palindrome('ишак ищет у тещи каши')) # True