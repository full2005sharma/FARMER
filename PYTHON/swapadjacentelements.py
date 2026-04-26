def swap_adjacent_elements(t):
    l = list(t)
    for i in range(0, len(l), 2):
        l[i], l[i+1] = l[i+1], l[i]
    return tuple(l)
print(swap_adjacent_elements((1,2,3,4,5,6)))