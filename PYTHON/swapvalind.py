def swap_last_chars_of_values(d: dict, k1, k2):
    v1 = d[k1]
    v2 = d[k2]
    d[k1] = v1[:-1] + v2[-1]
    d[k2] = v2[:-1] + v1[-1]
    return d
print(swap_last_chars_of_values({'a':'full','b':'Ani'}, 'a','b'))