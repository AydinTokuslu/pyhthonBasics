import random
sayi=random.randint(1,10)

can=int(input("kaç hak kullanmak istersiniz? : "))

hak=can
sayac=0

while (hak>0):
    sayac+=1
    tahmin=int(input("lütfen bir sayı giriniz : "))
    if (tahmin>sayi):
        print("daha küçük bir sayı giriniz")
    elif (sayi>tahmin):
        print("daha büyük bir sayı giriniz")
    else:
        print(f"tebrikler, {sayac}. seferde doğru tahmin ettiniz. toplam puanınız : {100-(100/can)*(sayac-1)}")
        break

    hak-=1
if hak==0:
    print(f"tüm haklarınız bitti, tutulan sayi : {sayi}")