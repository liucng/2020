
"""
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
A = a.lower()
text = input()
for text in a or A:
    if  text in a:
        t= ord(text)
        print(chr(t+3),end="")
    elif text in A:
        t = ord(text)
        print(chr(t + 3),end="")
    else:
        print(" ",end="")"""
"""from decimal import Decimal,getcontext
getcontext().prec = 17
result  = 3*Decimal(0.1)
print(type(result))
print(3*Decimal(0.1))
print(3*0.1)"""

#print("(3*4)+2",(3*4)+2,sep="=",end="=")

"""i = 0
code= 666666
while i<3:
    name = input("输入用户名：")
    key = eval(input("密码："))
    if name == "kate":
        if key ==code:
            print("登陆成功！")
            break
        else:
            i=i+1
    else:
        i=i+1
if i == 3:
    print("3次用户名或者密码均有误！退出程序。")
        # TODO: write code...
    # TODO: write code...
count = 0
"""
"""t = ""
for a in range(1,10):
    for b in range(0,10):
        for c in range(0,10):
            i =a*100+b*10+c
            if (i) ==(pow(a,3)+pow(b,3)+pow(c,3)):
                t+="{},".format(i)
print(t[:-1])"""

"""s = ""
for i in range(100, 1000):
    t = str(i)
    if pow(eval(t[0]),3) + pow(eval(t[1]),3) + pow(eval(t[2]),3) == i :
        s += "{},".format(i)
print(s[:-1])"""
"""for a in range(1,10):
    for b in range(0,11):
        for c in range(0,11):
            for d in range(0,11):
                t1=(a*1000+b*100+c*10+d)
                if t1==(pow(a,4)+pow(b,4)+c**4+d**4):
                    print(t1)"""
"""
i =2
s=0
while i<100:
    if i % 2 != 0 or i ==2:
        if i % 3 != 0 or i == 3:
            if i % 5 !=0 or i == 5:
                if i % 7 != 0 or i ==7:
                    s+=i
                    print("i:{},s:{}".format(i,s))
    i+=1
"""
