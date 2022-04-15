def hamming_weight(number):
    binary_code = bin(number).replace('0b', '') # Альтернатива строке слева
    count = 0                                   # binary_code = bin(number)[2:]
    for elem in binary_code:
        count += int(elem)
    return count


print(hamming_weight(0)) # 0
print(hamming_weight(4)) # 1
print(hamming_weight(101)) # 4
print(hamming_weight(255)) # 8