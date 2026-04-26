def modify_string_1(s: str) -> str:
    even = s[0::2]
    odd = s[1::2]
    return even + odd[::-1]
print(modify_string_1('full'))