def replace_vowels(s: str) -> str:
    vowels = 'aeiou'
    new = ''
    for ch in s.lower():
        if ch in vowels:
            new += '*'
        else:
            new += ch
    return new
print(replace_vowels('Sharmistha'))
