def most_common_char(words: list) -> str:
    freq = {}
    for word in words:
        for ch in word:
            freq[ch] = freq.get(ch, 0) + 1
    return max(freq, key=freq.get)
print(most_common_char(['hello','worlddooo']))