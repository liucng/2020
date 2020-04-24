height,weight = eval(input("输入身高(米)和体重(公斤)[逗号隔开]："))
bmi =weight/pow(height,2)
print("bmi为{:.2f}".format(bmi))
nat,who ="",""
if bmi <=18.5:
    who,nat="偏瘦","偏瘦"
    print("国际偏瘦，国内偏瘦")
elif bmi>18.5and bmi <=24:
    print("国际正常，国内正常")
    who, nat = "正常", "正常"
elif bmi >24and bmi <=25:
    print("国际正常，国内偏胖")
elif bmi >25and bmi<=28:
    print("国际正常，国内偏胖")
elif bmi >28and bmi<=30:
    print("国际偏胖，国内偏胖")
elif bmi >30:
    print("国际肥胖，国内肥胖")
else:
    print("错误")
print("bmi的国际指标为{0},国内指标为{1}".format(who,nat))