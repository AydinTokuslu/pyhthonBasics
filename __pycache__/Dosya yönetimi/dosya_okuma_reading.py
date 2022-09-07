# "r": (Read) okuma. Varsayılan dosya konumda yoksa hata verir. 

# try:
#     file=open("newfile.txt","r")
#     print(file)
# except FileNotFoundError:
#     print('dosya okuma hatası')
# finally:
#     print('dosya kapandı')
#     file.close()

file=open("newfile.txt","r", encoding="utf-8")

# for i in file:
#     print(i, end="")

#******************* read() fonksiyonu ***************
#read() fonksiyonu
# content1=file.read()
# print("içerik 1")
# print(content1)

# file=open("newfile.txt","r", encoding="utf-8")
# content2=file.read()
# print("içerik 2")
# print(content2)

# content=file.read(5)
# content=file.read(4)
# print(content)

#******************* readline() fonksiyonu ***************
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline())
# print(file.readline())
# print(file.readline())

#******************* readlines() fonksiyonu ***************
# liste=file.readlines()
# print(liste)
# print(liste[0])
# print(liste[1])
# print(liste[2])
# file.close()