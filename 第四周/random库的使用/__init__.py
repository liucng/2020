import random#用于生成随机数
"""基本随机数函数：seed(),random()
扩展随机数函数:randint(),getrandits(),uniform(),
randrange(),choice(),shuffle()"""
"""
random.seed()#产生种子<>对应的序列,<1>,<2>,<3>
random.random()#产生一个[0.0,1.0）之间的随机小数
random.randint(a,b)#生成一个[a,b]之间的整数
random.randrange(m,n[,k])生成一个[m,n)之间以k为步长的随机整数
random.getrandbits(K)#生成一个k比特长的随机整数
random.uniform(a,b)生成一个[a,b]之间的随机小数

random.choice(seq)#从序列seq中随机选择一个元素[1,2,3,4,5,6,7,8,9]
"""
s=[1,2,3,4,5,6,7,8,9]
random.shuffle(s)#将序列中元素随机排列，返回打乱后的序列
print(s)