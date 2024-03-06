import time as t

sec = t.time()
Years = sec / ( 365 * 60 * 60 * 24)
print(Years)

print(t.ctime())
print(t.localtime())
print(t.asctime())
print(t.gmtime())

FullDate = t.ctime()
print(FullDate.split(" "))

day = t.localtime().tm_mday
mon = t.localtime().tm_mon
year = t.localtime().tm_year
print(f"{day}/{mon}/{year}")