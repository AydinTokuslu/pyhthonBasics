import os
import datetime

result=dir(os)
result=os.name

#directory(dizin) değiştirme
#os.chdir('C:\\')
#os.chdir('..') BİR ÜST DİRECTORY E GEÇERİZ
#os.chdir('../..') en üst directory e geçeriz.

#klasör oluşturma
#os.mkdir("newdirectory")
#os.makedirs("newdirectory/yeniklasör")
# os.rename("newdirectory","yeniklasör")
# os.rmdir("newdirectory") klasör silme
# os.removedirs("yeniklasör/yeniklasör") alt klasörle beraber silme

#etkin dizin öğrenme
# result=os.getcwd()

#listeleme
# result=os.listdir()# etkin olan dizin içindeki klasörleri gösterir

#os.system('notepad.exe') #notepad açılır

print(result)