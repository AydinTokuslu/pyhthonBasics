maasAli = 5000
maasAhmet = 4000
vergi = 0.27

print(maasAli - (maasAli*vergi))
print(maasAhmet - (maasAhmet*vergi))

# değişken tanımlama kuralları
# sayısal ifade rakam ile başlayamaz

number1 = 10
print(number1)
number1 = 20
print(number1)

number1 += 30
print(number1)

# büyük küçük harf duyarlılığı vardır


age = 20
AGE = 30
print(age)
print(AGE)

X = 1  # int
Y = 2.3  # float
name = "ÇINAR"  # string
isStudent = True  # bool

# x,y,name,isStudent=(1,2.3,"çınar", True)


a = 10
b = 20
print(a+b)

a = '10'
b = '20'
print(a+b)  # 1020

firstname = "aydin"
lastname = " tokuslu"
print("adın soyadın : ", firstname+lastname)


pi = 3.14
r = float(input("yarı çap giriniz : "))
alan = pi * (r ** 2)
cevre = 2*pi*r
print("alan : ", alan)
print(type(alan))
print("çevre : ", cevre)
print(type(cevre))
print("alan : ", alan, "çevre : ", cevre)

print("alan : ", str(alan), "çevre : ", str(cevre))
