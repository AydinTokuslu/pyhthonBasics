#girilen bir sayının asal olup olmadığını bulun

sayi=int(input('sayı : '))

asalMi=True

if sayi ==1:
    print('1 sayısı asal değildir')
    

for i in range(2,sayi):
    if sayi%i==0:
        asalMi=False
        break

if asalMi:
    print('sayı asaldır')
else:
    print('sayı asal değildir')