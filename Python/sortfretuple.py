def word_freq(s: str) -> list:
    freq = {}
    for w in s.split():
        freq[w] = freq.get(w, 0) + 1
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))
print(word_freq('the cat and the dog'))