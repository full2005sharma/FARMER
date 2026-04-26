def flatten(t: tuple)->tuple:
    new_t = ()
    for i in t:
        new_t += i
    return new_t
print(flatten(((1,2),(3,4),(5,6))))