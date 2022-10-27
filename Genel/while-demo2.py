urunler=[]
adet=int(input("kaç adet urun eklemek istiyorsunuz? : "))
i=0

while i<adet:
    name=input("ürün adı giriniz: ")
    price=input("ürün fiyatı giriniz : ")
    urunler.append({
        "name":name,
        "fiyat": price
    })
    i+=1

for urun in urunler:
    print(f'urun adı : {urun["name"]}, urun fiyatı : {urun["fiyat"]}')