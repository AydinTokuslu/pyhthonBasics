#1- 'Bmw, mercedes, opel, mazda' elemanlarına sahip bir liste oluşturunuz
from tarfile import LENGTH_NAME
from unittest import result


arabalar=['Bmw', 'Mercedes', 'Opel', 'Mazda']
print(arabalar)

#2- liste kaç elemanlıdır
print(len(arabalar))
#3- listenin ilk ve son elemanı nedir?
print(arabalar[0])
print(arabalar[3])
print(arabalar[-1])
#4- mazda değerini toyota ile değiştirin
arabalar[-1]='Toyota'
result=arabalar
#5- mercedes listenin bir elemanı mıdır?
result='Mercedes' in arabalar
#6- listenin -2 indeksindeki değer nedir?
result=arabalar[-2]
#7- listenin ilk 3 elemanını alın
result=arabalar[0:3]
result=arabalar[:3]
result=arabalar[-2:]
#8- listenin son 2 elemanı yerine toyota ve renault değerlerini ekleyin
arabalar[2]='Toyota'
arabalar[3]='Renault'
arabalar[-2:]=['Toyota','Renault']
result=arabalar
#9- listenin üzerine audi ve nissan değerlerini ekleyin
result=arabalar + ['Audi', 'Nissan']
print(arabalar) #hala 4 elemanlı, listenin boyutunu değiştiremeyiz.

# 10- listenin son elemanını silin
del arabalar[-1]
result=arabalar
# 11- liste elemanlarını tersten yazdırın
result=arabalar[::-1]
# 12- aşağıdaki verileri bir liste içinde saklayınız
     # studentA: Yiğit Bilgi 2010, (70,60,70) 
     # studentB: Sena Turan 1999, (80,80,70) 
     # studentC: Ahmet Turan 1998, (80,70,90) 

studentA=['Yiğit', 'Bilgi', 2010, [70,60,70]]
studentB=['Sena', 'Turan', 1999, [80,80,70]]
studentC=['Ahmet', 'Turan', 1998, [80,70,90]]

#13- LİSTE ELEMANLARINI EKRANA YAZDIRIN
result=studentA[0]
result=studentB[1]
result=studentC[3][2]
print(studentC[3][2])

result=f"Yiğit Bilgi 9 yaşında ve not ortalaması 66"
result=f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}"

print(result)