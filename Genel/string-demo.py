from audioop import reverse
from dataclasses import replace
import re


website="http://www.sadikturan.com"
course = "Python Kursu : Baştan Sona Python Programlama Rehberiniz (40 saat)"

#1- 'course' karakter dizisinde kaç karakter bulunmaktadır.
result=len(course)
print(result)

#2- 'website' içinden www karakterlerini alın
print(website[7:10])

#3- 'website' içinden com karakterlerini alın
length=len(website)
print(website[-3:])
print(website[length-3:length])

#4- 'course' içinden ilk 15 ve son 15 karakterleri alın
print(course[:16])
print(len(course))
print(course[-16:])

#5- 'course' içinden karakterleri tersten yazdırın
result2=course[::-1]
print(result2)

s='12345' * 5
print(s[::5])

name, surname, age, job = 'Bora', 'Yılmaz', 32, 'mühendis'
#6- yukarıda verilen değişkenler ile ekrana aşağıdaki iafdeyi yazdırın
# 'Benim adım Bora Yılmaz, Yaşım 32 ve meslegim mühendis.'

print(f"Benim adım {name} {surname}, Yaşım {age} ve meslegim {job}.")
print("Benim adım {0} {1}, Yaşım {2} ve meslegim {3}.".format(name,surname, age, job))

# 7- 'Hello world' ifadesindeki w harfini W ile değiştirin
metin='Hello world'
metin=metin.replace('w','W')
print(metin)
#8- 'abc' ifadesini yan yana 3 defa yazdırın
r='abc ' * 3
print(r)








