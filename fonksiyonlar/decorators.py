# #decorator, bir fonksiyona özellik eklemek istediğimizde kullanıyoruz.
# #özelliği birkaç yerde kullanmak istiyorsak kullanırız @ ile gösterilir.

# def my_decorator(func):
#     def wrapper(name):
#         print("fonksiyondan önceki işlemler")
#         func(name)
#         print("fonksiyondan sonraki işlemler")
#     return wrapper

# @my_decorator
# def sayHello(name):
#     print("hello", name)

# # def sayGreeting():
# #     print("greeting")

# # sayHello=my_decorator(sayHello)
# # sayGreeting=my_decorator(sayGreeting)
# sayHello("ali")
# #sayGreeting()

import math
import time

def calculate_time(func):
    def inner(*args,**kwargs): #farklı çeşit parametreleri getirir.
        start=time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish=time.time()
        print("fonksiyon "+func.__name__+ " "+str(finish-start)+ " saniye sürdü.")
    return inner

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

@calculate_time
def toplama(a,b):
    print(a+b)

usalma(2,3)
faktoriyel(4)
toplama(10,20)