def words_after_the(s: str):
    words = s.split()
    result = []
    for i in range(len(words)-1):
        if words[i].lower() =='the':
            result.append(words[i+1])
    return result
print(words_after_the('this is the dog and the cat'))
