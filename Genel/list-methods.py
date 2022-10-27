numbers=[1,10,5,16,4,9,10]
letters=['a','g','s','b','y','a','s']

val=min(numbers)
val=max(numbers)
val=max(letters)
val=min(letters)

val=numbers[3:6]
val=numbers[:3]
val=numbers[4:]
numbers[4]=40

numbers.append(49)
numbers.append(59)
numbers.insert(3,78) #3ncü indexe 78 ekler
numbers.insert(-1,52)

numbers.pop() #ensondaki rakamı siler
numbers.pop(0) #0 indexindeki rakamı siler
numbers.remove(49) #belirtilen rakamı siler

numbers.sort() #sıralar
letters.sort() #alfabetik sıralar
numbers.reverse()
letters.reverse()

print(numbers)
print(len(numbers))

print(letters)
print(len(letters))

print(numbers.count(10)) #2
print(letters.count('a')) #2

numbers.clear()
print(numbers)

#print(val)