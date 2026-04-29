def count_vowels_and_consonants_in_even_indices(s: str) -> tuple:
    vc = 0
    cc = 0
    vowels = 'aeiou'
    for ch in s[0::2]:
        if ch.isalpha() and ch.lower() in vowels:
            vc += 1
        else:
            cc += 1
    return (vc, cc)
print(count_vowels_and_consonants_in_even_indices('Aniket'))

