def numwithmore_uni(n1: int, n2: int):
    s1 = len(set(str(n1)))
    s2 = len(set(str(n2)))
    if s1 > s2:
        return n1
    else:
        return n2
    
print(numwithmore_uni(123334,11111))