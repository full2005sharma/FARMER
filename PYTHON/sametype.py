def all_same_type(lst: list) -> bool:
    if not lst:
        return True
    ftype = type(lst[0])
    for l in lst:
        if type(l) != ftype:
            return False
    return True
        
print(all_same_type([1,2,3,'a']))