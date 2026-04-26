def unique_tuple(t: tuple) -> tuple:
    seen = set()
    l = []
    for i in t:
        if i not in seen:
            seen.add(i)
            l.append(i)
    return tuple(l)
print(unique_tuple((1,2,2,2,3,4,5,6,6,6,7,8)))