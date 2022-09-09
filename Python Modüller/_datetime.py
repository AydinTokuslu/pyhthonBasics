from datetime import datetime
from datetime import timedelta
# # from datetime import date
# # from datetime import time

# #import datetime

# # result=dir(datetime.datetime)
simdi=datetime.now()
# simdi=datetime.today()
# result=datetime.now()
# result=simdi.year
# result=simdi.month
# result=simdi.day
# result=simdi.hour
# result=simdi.minute
# result=simdi.second

# result=datetime.ctime(simdi)
# result=datetime.strftime(simdi,"%Y")
# result=datetime.strftime(simdi,"%X")
# result=datetime.strftime(simdi,"%A")
# result=datetime.strftime(simdi,"%A")
# result=datetime.strftime(simdi,"%d")
# result=datetime.strftime(simdi,"%Y %B %A")

# t='21 Nisan 2019'
# gun, ay, yil = t.split()
# print(gun)
# print(ay)
# print(yil)

t='21 April 2019 hour 10:12:30'
result=datetime.strptime(t, '%d %B %Y hour %H:%M:%S')

result=result.year

birthday=datetime(1983,5,9,12,30,10)

result=datetime.timestamp(birthday) #saniye
result=datetime.fromtimestamp(result) #saniye to datetime
result=datetime.fromtimestamp(0)

#iki tarih arasında farkı bulma
result=simdi - birthday #timedelta objesi

result=result.days #toplam gün bilgisi gelir
result=result.seconds #toplam saniye bilgisi gelir

#ileri bir tarihi bulmak istersek
result=simdi + timedelta(days=10) #şimdinin üzerine 10 gün ekleriz.
result=simdi + timedelta(days=10, minutes=10) #şimdinin üzerine 10 gün ekleriz.

result=simdi- timedelta(days=10)
print(result)
print(birthday)


# result=datetime.now()
# print(result)