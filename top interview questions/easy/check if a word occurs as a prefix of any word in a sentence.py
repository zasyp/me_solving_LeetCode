def isPrefixOfWord(sentence: str, searchWord: str):
    words = sentence.split()
    for i in range(len(words)):
        if words[i].startswith(searchWord):
            return i + 1

    return -1

print(isPrefixOfWord("i love eating burger", "burg"))