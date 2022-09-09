# # regular expression : re 

# import re

# # result=dir(re)

# # re module
# str="Python kursu: Python programlama rehberiniz | 40 saat"

# # re.findall()
# # result=re.findall("Python",str)

# # re.split()
# # result=re.split(" ", str)

# # re.sub (substring)
# # result=re.sub("","-",str)
# # 

# # re.search() arama
# # result=re.search("Python",str)

# # result=result.span() konumunu alırız.
# #result=result.start() 
# # result=result.end() 
# # result=result.group()
# # result=result.string()

# '''
# [abc]
# [sat]
# [a-e]
# [a-z]
# [0-5]
# [^abc] => abc dışındaki karakterler
# [^0-9] => rakam olmayan karakterler
# '''

# result=re.findall("[abc]",str) #abc karakterlerini arar 
# result=re.findall("[sat]",str) #sat karakterlerini arar
# result=re.findall("[a-e]",str) #a ile e arasındaki tüm karakterlerini arar
# result=re.findall("[a-z]",str) #a ile z arasındaki tüm karakterlerini arar
# result=re.findall("[0-5]",str) #0 ile 5 arasındaki tüm karakterlerini arar
# result=re.findall("[^abc]",str) #abc dışındaki tüm karakterlerini arar
# result=re.findall("[^0-9]",str) #rakam dışındaki tüm karakterlerini arar

# '''
# . - her hangi bir tek karakteri belirtir
# .. =>   a : no match
#         ab : 1 match
#         abc : 1 match
#         abcd : 2 matches

# '''

# # result=re.findall("...",str) #3 heceli kelimelere böler
# # result=re.findall("Py..on",str) 

# '''
# ^  - belirtilen string belirtilen karakter ile başlıyor mu?
# ^a =>   a : 1 match
#         abc : 1 match
#         bac : no match
# '''

# # result=re.findall("^P",str)

# '''
# $  - belirtilen string belirtilen karakter ile bitiyor mu?
# a$ =>   a : 1 match
#         lamba : 1 match
#         Python : no match
# '''
# # result=re.findall("t$",str)
# # result=re.findall("saat$",str)

# '''
# *  - bir karakterin sıfır ya da daha fazla sayıda olmasını kotrol eder
# ma*n =>   mn : 1 match
#         man : 1 match
#         maaan : 1 match
#         main : no match (a'nın arkasına n gelmiyor.)
# '''
# # result=re.findall("sa*t",str)

# '''
# +  - bir karakterin sıfır ya da daha fazla sayıda olmasını kotrol eder
# ma+n =>   mn : no match
#         man : 1 match
#         maaan : 1 match
#         main : no match (a'nın arkasına n gelmiyor.)
# '''
# # result=re.findall("sa+t",str)

# '''
# ?  - bir karakterin sıfır ya da bir kez olmasını kontrol eder
# ma?n =>   mn : no match
#         man : 1 match
#         maaan : 1 match
#         main : no match (a'nın arkasına n gelmiyor.)
# '''
# # result=re.findall("sa?t",str)

# '''
# {}  - karakter sayısını kontrol eder

#         al{2} : a karakterinin arkasına l karakteri 2 kez tekrarlanmalı
#         al{2,3} : a karakterinin arkasına l karakteri en az 2, en fazla 3 kez tekrarlanmalı
#         [0-9]{2,4} : en az 2, en çok 4 basamaklı sayılar        
# '''
# # result=re.findall("a{2}",str)
# # result=re.findall("a{2,3}",str)
# # result=re.findall("[0-9]{2}",str)

# '''
# | (or)  - alternatif seçeneklerden birinin gerçekleşmesi gerekir

#         a|b => a ya da b
#         cde => no match       
#         ade => 1 match       
#         acdbea => 3 match       
# '''
# # result=re.findall("a|b",str)

# '''
# ()  - gruplamak için kullanılır

#         (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir.     
# '''
# # result=re.findall("(a|b)t",str)

# '''
# \  - özel karakterleri aramamızı sağlar


# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	

# \b	Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
# r"ain\b"	

# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
# r"ain\B"	

# \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	

# \D	Returns a match where the string DOES NOT contain digits	"\D"	

# \s	Returns a match where the string contains a white space character	"\s"	

# \S	Returns a match where the string DOES NOT contain a white space character	"\S"	

# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	

# \W	Returns a match where the string DOES NOT contain any word characters	"\W"	

# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"
             
# '''





# print(result)