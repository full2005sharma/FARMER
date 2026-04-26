def invert_dict(d: dict) -> dict:
    new_d = {}
    for k, v in d.items():
        new_d[v] = k
    return new_d
print(invert_dict({'a': 1,'b': 2}))