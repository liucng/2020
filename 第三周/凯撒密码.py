i = str(input())
a = ""
for t in i :
    if "a"<= t <="z":
        a+=chr(ord("a")+(ord(t)-ord("a")+3)%26)
    elif "A"<= t <="Z":
        a+= chr(ord("A") + (ord(t) - ord("A") + 3) % 26)
    else:
        a=a+t
print(a)