def div_last_2(a: int):
    s = str(a)
    u = s[-1]
    v = s[-2]
    if u == '0' or v == '0':
        return False
    return a % int(u) == 0 and a % int(v) == 0
print(div_last_2(124))