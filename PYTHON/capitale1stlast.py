def capitalize_first_and_last(sentence: str) -> str:
    words = sentence.split()
    new_word = []
    for word in words:
        if len(word) > 1:
            new_word.append(word[0].upper() + word[1:-1] + word[-1].upper())
        else:
            new_word.append(word.upper())
    return ' '.join(new_word)
print(capitalize_first_and_last('hello world'))