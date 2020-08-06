m = input("enter microwave here: ")

for x in m:
    m = m.replace("v", "1")
    m = m.replace("m", "0")
    m = m.replace("V", "1")
    m = m.replace("M", "0")

for x in range((len(m)+7)//8):
    print(end = chr(int(m[x*8 : x*8+8], 2)) )
