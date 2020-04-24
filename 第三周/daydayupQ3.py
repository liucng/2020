dayup = float(input("输入百分比："))
y=1
daydown=float(input("输入下降百分比："))
for i in range(365):
    if i % 7 in [6,0]:
        y=(1-daydown)*y
    else:
        y=(1+dayup)*y
print("{:.2f}".format(y))

