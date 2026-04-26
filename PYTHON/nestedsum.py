def nested_sum(t: tuple) -> int:
    total = 0
    for i in t:
        total += sum(i)
    return total
print(nested_sum(((1,2),(3,1))))