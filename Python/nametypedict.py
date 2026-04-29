def count_by_type(lst: list) -> dict:
    r = {}
    for l in lst:
        t = type(l)
        r[t] = r.get(t, 0) + 1
    return r
print(count_by_type([1,2.0,'a']))