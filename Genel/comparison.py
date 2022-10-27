
# 1- girilen 2 sayıdan hangisi büyüktür?
#a=int(input("a sayısını giriniz : "))
#b=int(input("b sayısını giriniz : "))

#result= a > b
#print(f'a: {a}, b: {b} den büyüktür : {result}')

# 2- kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.eğer
# ortalama 50 ve üstünde ise geçti, değilse kaldı yazdırın
#vizeNotu1=float(input("1nci vize notunu giriniz : "))
#vizeNotu2=float(input("2nci vize notunu giriniz : "))
#finalNotu=float(input("Final notunu giriniz : "))

#ort = ((vizeNotu1+vizeNotu2)*0.60)/2 + (finalNotu*0.40)
#print(f'not ortalamanız : {ort}, ve dersten geçme durumunuz : {ort>=50}')

# 3- girilen bir sayının tek mi çift mi olduğunuz yazdırın
#sayi=int(input("sayı giriniz : "))
# tekCift=(sayi%2==0)
#print(f'girilen sayı çift olma durumu : {tekCift}')
# 4- girilen bir sayının negatif pozitif durumunu yazdırın
#sayi=int(input("sayı giriniz : "))
# pozitifMi=(sayi>0)
#print(f'girilen sayının pozitif olma durumu : {pozitifMi}')

# 5- parola ve email bilgisini isteyip doğruluğunu kontrol ediniz
# (email: emailmmmm@sadikturan.com parola:abc123)
email: 'mailll@sadikturan.com'
password: 'abc12345'

girilenEmail = input('email : ')
girilenPassword = input('password : ')

isEmail = (email == girilenEmail.lower())
isPassword = (password == girilenPassword.lower())

print(f'Email bilgisi doğru mu : {isEmail} ve parola doğru mu : {isPassword}')
