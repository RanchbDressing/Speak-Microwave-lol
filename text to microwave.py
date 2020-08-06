def string2bits(s=""):
    return [bin(ord(x))[2:].zfill(8) for x in s]
#converted text
s = input("enter text here: ")
b = string2bits(s)
b = str(b)

for x in b:
    b = b.replace("1", "v")
    b = b.replace("0", "m")

for x in b:
    b = b.replace("'", "",)
    b = b.replace(",", "",)
    b = b.replace(" ", "",)

print(b)


