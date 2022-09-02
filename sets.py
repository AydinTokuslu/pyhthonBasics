fruits={'orange', 'apple','banana'}

# print(fruits[0]) indexlenemez

for x in fruits:
    print(x)

fruits.add('cherry') #aynı elemanı 2 kere eklemez
fruits.update(['mango', 'grape','apple'])

fruits.remove('mango')
fruits.discard('apple')
fruits.pop()
fruits.clear()
print(fruits)

#myList=[1,2,3,4,5,2,1]
#print(myList)
#print(set(myList))