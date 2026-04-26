def char_freq(s: str) -> dict:
    d = {}
    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    return d
print(char_freq(('hello')))