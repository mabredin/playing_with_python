def build_query_string(dict: dict):
    value = []
    for i, k in sorted(dict.items()):
        value.append('{}={}'.format(i, k))
    return '&'.join(value)


print(build_query_string({'per': 10, 'page': 1})) # 'page=1&per=10'