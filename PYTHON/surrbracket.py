def surround_first_two_and_last_two_with_brackets(s: str):
    if len(s) < 4:
        return False
    return '['+s[0:2]+']'+s[2:-2]+'['+s[-2]+s[-1]+']'
print(surround_first_two_and_last_two_with_brackets('Hello'))