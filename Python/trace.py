def trace(matrix: list) -> int:
    s = 0
    for i in range(len(matrix)):
        s += matrix[i][i]
    return s
print(trace([[1,2],[3,4]]))
