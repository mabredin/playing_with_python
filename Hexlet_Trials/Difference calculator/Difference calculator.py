def gen_diff(first: dict, second: dict):
    first_set = set(first.keys())
    second_set = set(second.keys())
    third = {}
    shared_keys = first_set.intersection(second_set)
    third.update({o: 'deleted' for o in first_set - second_set})
    third.update({o: 'added' for o in second_set - first_set})
    third.update({o: 'changed' for o in shared_keys if first[o] != second[o]})
    third.update({o: 'unchanged' for o in shared_keys if first[o] == second[o]})
    return third


print(gen_diff(
    {"one": "eon", "two": "two", "four": True},
    {"two": "own", "zero": 4,
     "four": True}, ))  # {"one": "deleted", "two": "changed", "four": "unchanged", "zero": "added"}
