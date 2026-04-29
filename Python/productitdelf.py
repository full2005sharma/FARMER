def product_except(lst: list) -> list:
    n = len(lst)
    result = [1]*n
    left = 1
    for i in range(n):
        result[i] *= left
        left *= lst[i]
    right = 1
    for i in range(n-1, -1, -1):
        result[i] *= right
        right *= lst[i]
    return result
print(product_except([1,2,3,4]))