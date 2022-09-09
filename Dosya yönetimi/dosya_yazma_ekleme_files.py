# dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# kullanımı : open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir

# "w": (Write) yazma modu. Dosyayı konumda oluşturur.
#    ** Dosyayı konumda oluşturur
#    ** Dosya içeriğini siler ve yeniden ekleme yapar.


# file=open("newfile.txt","w") # dosya hiç olmadığı için önce oluşturuyoruz
#file=open("C:/Users/aydin/Desktop/newfile.txt","w") #masaüstünde dosya oluşturma

#file.close() # dosyayı açtıktan, bilgileri girdikten sonra dosyayı kapatmamız gerekiyor.
# file=open("newfile.txt","w", encoding='utf-8')
# # file.write("aydin tokuslu")
# file.close()

# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
# file=open("newfile.txt","a", encoding='utf-8')
# # file.write("\nelif tokuslu")
# file.write("elif tokuslu\n")
# file.close()

# "x": (Create) oluşturma. Dosya zaten varsa hata verir.
file=open("newfile2.txt","x", encoding='utf-8')
file.close()


# "r": (Read) okuma. Varsayılan dosya konumda yoksa hata verir. 