

#1- girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

#sayi=int(input('sayi giriniz : '))
#result = sayi>0 and sayi <100
#print(f"girdiğiniz {sayi} sayısının 0 ile 100 arasında olma durumu : {result}")

#2-
#sayi=int(input('sayi giriniz : '))
#result = sayi>0 and sayi%2==0
#print(f"girdiğiniz {sayi} sayısının pozitif ve çift olma durumu : {result}")

#3-
#email='email@hasan'
#password='123abc'
#girilenEmail=input('email : ')
#girilenPassword=input('password : ')
#result=(girilenEmail==email) and (girilenPassword==password)
#print(f'uygulamaya giriş başarılı mı : {result}')

#4-
#a=int(input('a sayi giriniz : '))
#b=int(input('b sayi giriniz : '))
#c=int(input('c sayi giriniz : '))
#result=(a>b) and (a>c)
#print(f'a en büyük sayıdır : {result}')
#result=(b>a) and (b>c)
#print(f'b en büyük sayıdır : {result}')
#result=(c>a) and (c>b)
#print(f'c en büyük sayıdır : {result}')

#5-
#vize1=float(input('vize1: '))
#vize2=float(input('vize2: '))
#final=float(input('final: '))

#ort=((vize1+vize2)/2)*0.6 + (final*0.4)
#result=ort>=50 and final>=50
#result=ort>=50 or final>=70
#print(f'öğrencinin ortalaması : {ort} ve geçme durumu : {result}')

#6-
name=input('adınız : ')
kg=float(input('kilonuz : '))
hg=float(input('boyunuz : '))

index=(kg) / (hg ** 2)
zayif=(index>=0) and (index<=18.4)
normal=(index>18.4) and (index<=24.9)
kilolu=(index>24.9) and (index<=29.9)
obez=(index>29.9) and (index<=34.9)

print(f'{name} kilo indexin : {index} ve kilo değerlendirmen  zayıf : {zayif}')
print(f'{name} kilo indexin : {index} ve kilo değerlendirmen  normal : {normal}')
print(f'{name} kilo indexin : {index} ve kilo değerlendirmen  kilolu : {kilolu}')
print(f'{name} kilo indexin : {index} ve kilo değerlendirmen  obez : {obez}')









