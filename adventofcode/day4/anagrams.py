def anagram(phrases):
    sorted_phrase = []
    for word in phrases.split(" "):
        if sorted(word) in sorted_phrase:
            return False
        sorted_phrase.append(sorted(word))
    return True


if "__main__" in __name__:
    with open("passphrase") as passphrase:
        c = 0
        for words in passphrase.readlines():
            if anagram(words[:-1]):
                c += 1
    print(c)
