def longest_list_key(d: dict):
    return max(d, key=lambda k: len(d[k]))
print(longest_list_key({'a': [2],'b': [1,2,3]}))