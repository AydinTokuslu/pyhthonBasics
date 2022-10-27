x,y,z=2,5,10

numbers=1,5,7,10,6
#1- kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?
#a=int(input("bir a sayı giriniz : "))
#b=int(input("bir b sayı giriniz : "))

#result=(a*b)-(x+y+z)

#2- y nin x e kalansız bölümünü hesaplayınız
#result=y//x

#3- (x,y,z) toplamının mod 3 ü nedir?
result=(x+y+z)%3
#4- y nin x. kuvvetini hesaplayınız
result=y**x
#5- x, *y, z = numbers işlemine göre z nin küpü nedir?
x, *y,z=numbers
result=z**3
#6- x, *y, z = numbers işlemine göre y nin değerleri toplamı nedir?
result=y[0]+y[1]+y[2]

print(result)