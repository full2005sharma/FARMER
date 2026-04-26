def interleave_strings(s1: str, s2: str) -> str:
    result = []
    i = 0
    while i < len(s1) and i < len(s2):
        result.append(s1[i])
        result.append(s2[i])
        i += 1
    result.append(s1[i:])
    result.append(s2[i:])
    return ''.join(result)
print(interleave_strings('abc','12334567'))