def pivot(data: list) -> dict:
    r = {}
    for c, v in data:
        r[c] = r.get(c, 0) + v
    return r
print(pivot([('A',20),('B',10),('C',5)]))