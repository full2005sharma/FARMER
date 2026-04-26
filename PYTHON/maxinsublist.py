def max_in_sub(l: list):
    return max(max(sub) for sub in l)
print(max_in_sub([[2,3],[9,10]]))