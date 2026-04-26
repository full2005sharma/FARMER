def symmetric_difference(lst1: list, lst2: list) -> set:
    s1 = set(lst1)
    s2 = set(lst2)
    s3 = s1 & s2
    s4 = s1 | s2
    s5 = s4 - s3
    return s5
    
print(symmetric_difference([1,2,3],[3,4,5]))