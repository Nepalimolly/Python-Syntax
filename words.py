def all_upper(words):
    for word in words:
        print(word.upper())

def all_upper_starts(words):
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())

def all_upper_choose(words, starts_with):
    for word in words:
        for letter in starts_with:
            if word.startswith(letter):
                print(word.upper())
                break

