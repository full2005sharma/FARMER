def invert_dict(d: dict) -> dict:
    r = {}
    for k, vals in d.items():
        for v in vals:
            if v not in r:
                r[v] = []
            r[v].append(k)
    return r
print(invert_dict({'a':[1,2],'b':[2,3]}))