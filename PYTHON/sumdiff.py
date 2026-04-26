def sum_abs_diff(a: int):
    s = str(abs(a))
    b = int(s[0]) + int(s[-1])
    c = abs(int(s[0]) - int(s[-1]))
    return b*c
print(sum_abs_diff(54))