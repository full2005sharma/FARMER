def partition(lst: list) -> tuple:
    yes = []
    no = []
    for l in lst:
        if l % 2 == 0:
            yes.append(l)
        else:
            no.append(l)
    return(yes, no)
print(partition([1,2,3,4,5,6]))