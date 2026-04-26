def second_largest(lst: list) -> int:
    new_list = sorted(lst)
    return new_list[-2]
print(second_largest([2,10,3,1,9]))