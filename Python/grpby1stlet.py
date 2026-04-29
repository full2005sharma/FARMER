def group_by_first(words: list) -> dict:
    g = {}
    for word in words:
        k = word[0].lower()
        if k not in g:
            g[k] = []
        g[k].append(word)
    return g
print(group_by_first(['apple','ant','kiwi']))