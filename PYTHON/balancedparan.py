def balanced_paranthesses(s: str):
    count = 0
    for i in s:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0
print(balanced_paranthesses('(((((()))))'))