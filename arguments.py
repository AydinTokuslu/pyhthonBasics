# def changeName(n):
#     n='ada'

# name='yigit'

# changeName(name)
# print(changeName(name))
# print(name)

# def change(n):
#     n[0]='istanbul'

# sehirler=['ankara','izmir']
# change(sehirler[:])
# print(sehirler)

# def add(a,b,c=0,d=0,e=0):
#     return sum((a,b,c))

# print(add(10,20))
# print(add(10,20,30))
# print(add(10,20,30,40))

# def add(*params):
#     print(params)
#     return sum((params))

# print(add(10,20))
# print(add(10,20,30))
# print(add(10,20,30,40,60,10,80))

# def add(*params): #liste olduğunu belirtmek için * kullanırız, dictionary olsaydı ** olacaktı
#     sum=0
#     for n in params:
#         sum+=n  
#     return sum

# print(add(10,20))
# print(add(10,20,30))
# print(add(10,20,30,40,60,10,80))

def displayUser(**params): #dictionary olduğu için ** olacaki params veya args olabilir.
    for key, value in params.items():
        print('{} is {} '.format(key,value))

displayUser(name='çınar', age=2, city='istanbul')
displayUser(name='ahmet', age=12, city='kocaeli', phone='1225')
displayUser(name='veli', age=32, city='mersin', phone='1225',email='ayhan@gmail.com')

def myfunc(a,b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myfunc(10,20,30,40,50, key1='value1', key2='value2')

