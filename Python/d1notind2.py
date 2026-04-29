def dict_diff(d1: dict, d2: dict) -> dict:
    return {k: v for k, v in d1.items() if k not in d2}
print(dict_diff({'a':1,'b':4},{'b':2,'c':8}))