def valid_substring(s: str, word_list: list) -> bool:
    for i in range(1, len(s)):
        if s[:i] in word_list and s[i:] in word_list:
            return True
    return False
print(valid_substring('fullsharma',['full','sharma']))