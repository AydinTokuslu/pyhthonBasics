with open("newfile2.txt","r", encoding="utf-8") as file:  #utf-8 türkçe karakterlerin de okunmasını sağlar.
    content=file.read(10)
    print(content)
    file.seek(0) #seek() cursor nereye gitsin komutu, 0'a gönderririz.
    print(file.tell())# tell() cursorun konumunu verir.
    content2=file.read()
    print(content2)
    
# with ile file.close() dememeize gerek yok, kod çalışıp bitince hemen file kapanıyor.

