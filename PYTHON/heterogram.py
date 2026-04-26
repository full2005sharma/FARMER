def is_heterogram(sentence: str) -> bool:
    words = sentence.split()
    new = []
    for word in words:
        for w in word.lower():
            if w.isalpha():
                new.append(w)
    if len(new) == len(set(new)):
        return True
    else:
        return False
print(is_heterogram('they saw us'))