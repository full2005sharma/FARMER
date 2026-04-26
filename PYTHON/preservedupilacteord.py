def remove_dups(lst: list) -> list:
    seen = set()
    l = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            l.append(x)
    return l
print(remove_dups([3,1,2,1,6,4,5]))