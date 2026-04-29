def list_to_nested(keys: list, value):
    r = value
    for k in reversed(keys):
        r = {k: r}
    return r
print(list_to_nested(['a','b'], 2))
