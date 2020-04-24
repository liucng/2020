"""n=int(input())
print("{:-^20}".format(pow(n,3)))"""
def daywork(dayup):
    daywork=1.0
    for day in range(365):
        if day%7 in [0,6]:
            daywork=(1-0.01)*daywork
        else:
            daywork=(1+dayup)*daywork
    return daywork
dayup=0.01
while daywork(dayup)<37.78:
    dayup+=0.001
print("工作日的努力参数是:{:.3f}".format(dayup))