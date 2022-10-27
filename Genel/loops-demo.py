#sayı tahmin oyunu, 1-100 arasında sayı bulma

#random modülü ile

import random

sayi=random.randint(1,10)

can=int(input('kaç hak kullanmak istersiniz : '))

hak=can
sayac=0
while hak>0:
    sayac+=1
    hak-=1
    sayiTahmin=int(input('sayı tahmini giriniz: '))
    if sayiTahmin==sayi:
        print(f'tebrikler {sayac}. defada doğru tahmin ettiniz. Toplam puanınız : {100 - (100/can)*(sayac-1)}')
        break
    elif sayiTahmin<sayi:
        print('yukarı sayı giriniz')
    else:
        print('aşağı sayı giriniz')
    
if hak==0:
    print(f'tüm haklarınız bitti, tutulan sayı : {sayi}')