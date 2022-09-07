import random

# result=dir(random)

# result=random.random()*100
result=int(random.uniform(10,100))
result=random.randint(1,10)

greeting='hello there'
names=['ali','yagmur','deniz','cenk','efe','aydin','sare']
# result=names[random.randint(0,len(names)-1)]
result=random.choice(names)
# result=random.choice(greeting) #hello there tüm karakterleri tek tek yazdırır.

liste=list(range(10))
random.shuffle(liste) #sayıların yerlerini değiştirir.

result=liste

liste=range(100)
result=random.sample(liste,3) #sample, rastgele istediğimiz kadar sayı getirir.burda 3 sayı

result=random.sample(names,2)

print(result)