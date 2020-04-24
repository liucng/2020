i = input("输入：向上还是向下")
if i[0:] in ['向上',"x"]:
    x =pow(1.001,365)
    print("向上:{:.2f}".format(pow(1.001,365)))
elif i[0:] in ['向下','z']:
    print("{:.2f}".format(pow(0.999,365)))
else:
    print("错误")
