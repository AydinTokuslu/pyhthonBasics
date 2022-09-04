#fonksiyonun kısaltılmışı = def

def sayHello(name='user'):
    return 'Hello '+name


msg=sayHello('Aydin')
#sayHello()
print(msg)

def total(num1,num2):
    return num1+num2

result=total(10,20)
print(result)

def yasHesapla(dogumYili):
    return 2019-dogumYili

ageCinar=yasHesapla(2017)
ageAda=yasHesapla(2010)
ageSena=yasHesapla(1999)

print(ageCinar,ageAda,ageSena)


def emekliligeKacYilKaldi(dogumYili, isim):
    '''
    DOCSTRING : Dogum yiiniza gore emekliliginize kac yil kaldi
    INPUT : Dogum yili
    OUTPUT : Hesaplanan yil bilgisi
    '''
    yas=yasHesapla(dogumYili)
    emeklilik=65 - yas

    if emeklilik>0:
        print(f'emekliliğinize {emeklilik} yıl kaldı')
    else:
        print('zaten emekli oldunuz')


emekliligeKacYilKaldi(1983, 'Ali')
emekliligeKacYilKaldi(1965, 'Ahmet')

print(help(emekliligeKacYilKaldi))


list=[1,2,3]
print(help(list.append))






