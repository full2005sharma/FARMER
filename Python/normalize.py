def normalize(lst: list) -> list:
    mn = min(lst)
    mx = max(lst)
    if mn == mx:
        return [0.0]*len(lst)
    return [(l-mn)/(mx-mn) for l in lst]
print(normalize([2,4,6]))
