import time as t
t.time()#获取当前时间戳，计算机内部时间值，浮点数
t.ctime()#获取当前时间以易读方式，返回字符串
t.gmtime()#获取当前时间，表示为计算机可处理的时间格式
t.strftime("%Y-%m-%d %H:%M:%S")
"""strftime(tpl,ts) tpl是格式化模板字符串，用来定义输出效果，ts是计算机内部时间类型变量"""
"""t=gmtime()
time.sstrftime("%Y-%m-%d %H:%M:%S",t)
%Y-年份
%m-月份   %B  月份名称   %b  月份名称的缩写
%d 日期   %A  星期  %a   星期缩写 
%H   小时（24小时制） %i  （12小时制）%p  AM ，PM上午下午
:%M（分）:%S（秒）        
"""
#timeStr='2020-04-06 11:35:43'   t.strptime(timeStr,"%Y-%m-%d %H:%M:%S")
#t.strptime(str,tpl)              2020-04-06
# time.struct_time(tm_year=2020, tm_mon=4, tm_mday=6, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=97, tm_isdst=-1)
"""Start=t.perf_counter()           计时
end=t.perf_counter_ns()
end-Start"""
def wait():
    t.sleep(3.3)
wait()#等待3.3秒再退出运行