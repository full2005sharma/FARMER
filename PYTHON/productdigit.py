def product_of_digit(n: int):
    s = str(n)
    value = 1
    for i in s:
        value *= int(i)
    return value
print(product_of_digit(123))
