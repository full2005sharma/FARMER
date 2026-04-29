def most_frequent_element(lst: list) -> int:
    freq = {}
    for l in lst:
        freq[l] = freq.get(l, 0) + 1
    maxs = max(freq.values())
    big = [k for k, v in freq.items() if v == maxs]
    return max(big)
print(most_frequent_element([1,2,2,2,3,3,3,3,3,5,6]))