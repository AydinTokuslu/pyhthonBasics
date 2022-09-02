x=5
hak=5
devam='e'

#and
#True, True => True
#True, False => False
result=(x > 5) and (x < 10) #her tarafında true olması gerekiyor 
result=(hak>0) and (devam=='e')

#or
#True, True => True
#True, False => True
#False, False => False
result=(x>0) or (x%2==0)

#not
#True, True => True
#True, False => False
result=not(x>0) #cevabı tam tres cevaba çevirir.


#x, 5-10 arasında olan bir çift sayı mıdır?
result=((x>5) and (x<10)) and (x%2==0)


print(result)