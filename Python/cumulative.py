def cum_product(lst: list) -> list:
    r = []
    c = 1
    for l in lst:
        c *= l
        r.append(c)
    return r
print(cum_product([1,2,3,4]))
