# with open("newfile.txt","r+", encoding="utf-8") as file: #r+ komutu, hem okuma hem yazma komutu demek
#     print(file.read())

# with open("newfile.txt","r+", encoding="utf-8") as file: #r+ komutu, hem okuma hem yazma demek
#     file.seek(20)
#     file.write("deneme") # "r+"" yerine, w (write) yazsa idik, içindeki herşeyi silip en baştan "deneme" yazacaktı

# with open("newfile.txt","r+", encoding="utf-8") as file: #r+ komutu, hem okuma hem yazma demek
#     print(file.read())

# ****** sayfa sonunda güncelleme ************

# with open("newfile.txt","a", encoding="utf-8") as file:  #a : append, sayfanın en sonuna gelip ekleme yapar
#     file.write("\nemel turan")

# ****** sayfa başında güncelleme ************

# with open("newfile.txt","r+", encoding="utf-8") as file:
#     content=file.read()
#     content= "efe turan\n" + content 
#     file.seek(0)
#     file.write(content)




# ****** sayfa ortasında güncelleme ************
# with open("newfile.txt","r+", encoding="utf-8") as file: 
#     list=file.readlines()
#     list.insert(1,"ali korkmaz\n") #1 den önce ekler
#     file.seek(0)
#     for i in list:
#         file.write(i)

with open("newfile.txt","r+", encoding="utf-8") as file: 
    list=file.readlines()
    list.insert(1,"yılmaz karabacak\n") #1 den önce ekler
    file.seek(0)
    file.writelines(list)

with open("newfile.txt","r", encoding="utf-8") as file: 
     print(file.read())
