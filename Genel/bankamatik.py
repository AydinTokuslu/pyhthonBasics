#bankamatik uygulaması

SadikHesap={
    'ad':'sadık turan',
    'hesapNo':'13245678',
    'bakiye':3000,
    'ekHesap':2000
}

AliHesap={
    'ad':'ali turan',
    'hesapNo':'12345678',
    'bakiye':2000,
    'ekHesap':1000
}

def paraCek(hesap, miktar):
    print(f"merhaba {hesap['ad']}")

    if(hesap['bakiye']>=miktar):
        hesap['bakiye']-=miktar
        print('paranızı alabilirsiniz')
        bakiyeSorgula(hesap)
    else:
        toplam=hesap['bakiye']+hesap['ekHesap']
        if toplam>=miktar:
            ekHesapKullanimi=input('ek hesap kullanılsın mı (e/h)')

            if ekHesapKullanimi =='e':
                ekHesapKullanilacakMiktar= miktar - hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekHesap']-= ekHesapKullanilacakMiktar
                print('paranızı alabilirsiniz')
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} tl paranız bulunmaktadır")
        else:
            print('üzgünüz bakiyeniz yetersizdir.')
            bakiyeSorgula(hesap)


def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} tl bulunmaktadır. ek hesap limitiniz ise {hesap['ekHesap']} tl bulunmaktadır.")

paraCek(SadikHesap,2000)
bakiyeSorgula(SadikHesap)
#paraCek(SadikHesap,3000)




