def smart_title(s: str):
    lists = ['a','an','for','the','and','but','in','is']
    words = s.split()
    l = []
    for i, word in enumerate(words):
        if i == 0 or word.lower() not in lists:
            l.append(word.capitalize())
        else:
            l.append(word.lower())
    return ' '.join(l)
print(smart_title('she is lord'))