def to_rna(item):
    dict = []
    for i in item:
        if i == 'G':
            dict.append('C')
        if i == 'C':
            dict.append('G')
        if i == 'T':
            dict.append('A')
        if i == 'A':
            dict.append('U')
    return ''.join(dict)


print(to_rna('ACGTGGTCTTAA')) # 'UGCACCAGAAUU'