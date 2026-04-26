def pascal_to_snake(s: str) -> str:
    new = [s[0].lower()]
    for ch in s[1:]:
        if ch.isupper():
            new.append('_')
            new.append(ch.lower())
        else:
            new.append(ch)
    return ''.join(new)
print(pascal_to_snake('HelloWorld'))