def microwave():
    p = input("enter 1 or 2 for desired operation: ")
    a = ("1")
    c = ("2")

    def string2bits(s=""):
        return [bin(ord(x))[2:].zfill(8) for x in s]

    def t2m():
        def string2bits(s=""):
            return [bin(ord(x))[2:].zfill(8) for x in s]

        # converted text

        return b

    if p is a:
        s = input("enter text here: ")
        b = string2bits(s)
        b = str(b)
        t2m()
        for x in b:
            b = b.replace("1", "v")
            b = b.replace("0", "m")

        for x in b:
            b = b.replace("'", "", )
            b = b.replace(",", "", )
            b = b.replace(" ", "", )
        print(b)
        print("\n")
        microwave()
    elif p is c:
        m = input("enter microwave here: ")

        for x in m:
            m = m.replace("v", "1")
            m = m.replace("m", "0")
            m = m.replace("V", "1")
            m = m.replace("M", "0")

        for x in range((len(m) + 7) // 8):
            print(end=chr(int(m[x * 8: x * 8 + 8], 2)))
        print("\n")
        microwave()
    else:
        microwave()
    return("hacker")

microwave()