import re


website="http://www.sadikturan.com"
course = "Python Kursu : Baştan Sona Python Programlama Rehberiniz (40 saat)"

#1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin
result=' Hello World '.strip()
result=' Hello World '.lstrip()
result=' Hello World '.rstrip()

result=website.lstrip('/:pth')


#2- 'www.sadıkturan.com' içindeki sadikturan bilgisi haricindeki her kaarkteri silin
result='www.sadıkturan.com'.strip('w.com')

#3- 'course' karakter dizisinin tüm karakterlerini küçük harf yapın
result=course.lower()
result=course.upper()
result=course.title()

#4- 'website' içinde kaç tane a karakteri vardır
result=website.count('a')
result=website.count('a', 0,10)

#5- 'website' www ile başlayıp com ile bitiyor mu?
result=website.startswith('www')
result=website.endswith('com')

#6- 'website' içinde .com ifadesi var mı?
result=website.__contains__('.com')
result=website.find('com')
result=course.find('saat')
result=course.rfind('saat')
result=website.index('com')
result=website.rindex('com')

#7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
result=course.isalpha() #false
result='Hello'.isalpha() #true
result=course.isdigit() #false
result='123'.isdigit() #true 

#8- 'contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz
result='contents'.center(50,'*')
result='contents'.ljust(50,'*')
result='contents'.rjust(50,'*')

#9- 'course' karakter dizisindeki tüm boşluk karakterlerini - ile değiştirin
result=course.replace(' ','-')
result=course.replace(' ','-',5)
result=course.replace(' ','')

#10- 'Hello World' karater dizisinin 'World' ifadesini 'There' olarak değiştirin
result='Hello World'.replace('World','There')

#11- 'course' karakter dizisini boşluk karakterlerinden ayırın
result=course.split(' ')
result=result[3]

print(result)