def checker(word):
    keymap = {}
    for i in word:
        if i in keymap:
            return i
        keymap[i] = 1
    return None

