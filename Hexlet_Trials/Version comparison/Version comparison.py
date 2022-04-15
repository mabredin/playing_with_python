def compare_version(version1, version2):
    first_list = version1.split('.')
    second_list = version2.split('.')
    count = 0
    for index, elem in enumerate(first_list):
        if int(first_list[index]) > int(second_list[index]):
            count = 1
            return count
        elif int(second_list[index]) > int(first_list[index]):
            count = -1
            return count
    return count


print(compare_version('1.2', '0.12')) # 1
print(compare_version('0.2', '0.12')) # -1
print(compare_version("0.1", "0.2")) # -1
print(compare_version("0.2", "0.1")) # 1
print(compare_version("4.2", "4.2")) # 0