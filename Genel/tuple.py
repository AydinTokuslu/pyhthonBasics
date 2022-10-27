list=[1,2,3]

tuple = (1, 'iki',3) #tuple elemanlar atandıktan sonra bir değişiklik, ekleme, çıkarma yapamıyoruz, array gibi

print(type(list))
print(type(tuple))

print(list[2])
print(tuple[2])

print(len(list))
print(len(tuple))

list=['ali', 'veli']
tuple=('damla','ayşe','ayşe')
#tuple[3]='hasan'  ekleme yapamayız.
print(list)
print(tuple)
print(tuple.count('ayşe'))

names=('demet','emel','ayşe') + tuple
print(names)

