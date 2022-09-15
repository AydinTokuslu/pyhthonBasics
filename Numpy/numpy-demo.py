from unittest import result
import numpy as np

# 1-
# result= np.array([10,15,30,45,60])
# # 2-
# result=np.arange(5,15)
# # 3-
# result=np.arange(50,100,5)
# # 4-
# result=np.zeros(10)
# # 5-
# result=np.ones(10)
# # 6- 
# result=np.linspace(0,100,5) # eşit aralıklı 5 sayı üretilir.
# # 7-
# result=np.random.randint(10,30,5)
# # 8-
# result=np.random.randn(10) #randn -1 ile 1 arasında sayı üretir
# # 9-(3x5) boyutlarında (10-50) arasında rastgele bir matris oluşturunuz.
# result=np.random.randint(10,50,15).reshape(3,5)
# 10-
matris=np.random.randint(-50,50,15).reshape(3,5)
# rowTotal=matris.sum(axis=1)
# colTotal=matris.sum(axis=0)
# print(rowTotal)
# print(colTotal)
# 11-
# result=matris.max()
# result=matris.min()
# result=matris.mean()
# # 12-
# result=matris.argmax() #üretilen max değerin indexini verir
# result=matris.argmin() #üretilen min değerin indexini verir
# 13-
# arr=np.arange(10,20)
# print(arr)
# result=arr[0:3]
# # 14-
# result=arr[::-1] #üretilen sayıları tersten yazdırır.
# # 15-üretilen matrisin ilk satırını seçiniz
# result=matris[0]
# # 16- üretilen matrisin 2.satır 3.sutundaki eleman hangisidir?
# result=matris[1,2]
# # 17-üretilen matrisin tüm satırlardaki ilk elemanı seçiniz
# result=matris[:,0]
# # 18-üretilen matrisin her bir elemanının karesini alınız
# result=matris ** 2
# 19-üretilen matris elemanlarının hangisi pozitif çift sayıdır?
# aralığı (-50,+50) arasında yapınız.
ciftler=matris[matris % 2 == 0]
result=ciftler[ciftler>0]



print(result)