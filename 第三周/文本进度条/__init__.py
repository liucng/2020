import time
t=20
print("\r"+"开始".center(t//2,"-"))
start=time.perf_counter()
for i in range(t//2+1):
    a="-"*i
    b=">"*(t//2-i)
    c=(i/10)*100
    e=time.perf_counter()-start
    print("\r{:^3.0f}%[{}{}]{:.2f}s".format(c,a,b,e),end="")
    time.sleep(0.2)
"""for i in range(101):
    print("\r{:5}%".format(i),end="")
    time.sleep(0.1)"""
print("\n"+"完成".center(10,"-"))