def is_vow(inp):

    for i in inp:
        if i == 97:
            y = inp.index(i)
            inp.remove(i)
            inp.insert(y, "a")
        
        if i == 101:
            y = inp.index(i)
            inp.remove(i)
            inp.insert(y, "e")
        
        if i == 105:
            y = inp.index(i)
            inp.remove(i)
            inp.insert(y, "i")

        if i == 111:
            y = inp.index(i)
            inp.remove(i)
            inp.insert(y, "o")

        if i == 117:
            y = inp.index(i)
            inp.remove(i)
            inp.insert(y, "u")

    return inp
        
print(is_vow([118,117,120,121,117,98,122,97,120,106,104,116,113,114,113,120,106]))