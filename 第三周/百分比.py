增加 = input("是否增加还是减少：")

if 增加[0:] in ['增加']:
    i = float(input("输入百分比："))
    print("增加：{:.2f}".format(pow((1.0+i),365)))
elif 增加[0:] in['减少']:
    i = float(input("输入百分比："))
    print("减少：{:.2f}".format(pow((1.0-i),365)))
else:
    print('输入错误')