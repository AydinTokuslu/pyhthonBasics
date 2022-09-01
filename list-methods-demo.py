from cgitb import reset


names=['Ali', 'Yagmur','Hakan','Deniz']
years=[1998,2000,1998,1987]

#1- cenk ismini listenin sonuna ekleyiniz
names.append('Cenk')

#2- sena değerini listenin başına ekleyiniz
names.insert(0,'Sena')
#3- deniz ismini listeden siliniz
names.remove('Deniz')
#4- deniz isminin indexi nedir?
names.append('Deniz')
index=names.index('Deniz')
print(index)
# 5- ali listenin bir elemanı mıdır?
result='Ali' in names
result=names.index('Ali')
print(result)
# 6- liste elemanlarını ters çevirin
names.reverse()
# 7- liste elemanlarını  alfabetik olarak sıralayınız
names.sort()
# 8- years lsitesini rakamsal büyüklüğe göre sıralayınız
years.sort()
# 9- str="chevrolet, dacia" karakter dizisini listeye çeviriniz
str="chevrolet, dacia"
result=str.split(',') 
print(result)
# 10- years dizisinin en büyük ve en küçük elemanı nedir?
min=min(years)
print(min)
max=max(years)
print(max)
# 11- years dizisinde kaç tane 1998 değeri vardır?
result=years.count(1998)
print(result)
# 12- years dizisinin tüm elemanlarını siliniz
years.clear()
print(years)
# 13- kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız  

markalar=[]
marka=input("marka: ")
markalar.append(marka)

marka=input("marka: ")
markalar.append(marka)

marka=input("marka: ")
markalar.append(marka)


print(markalar)

#print(names)
#print(years)