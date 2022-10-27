# name='aydin'

# for letter in name:
#     if letter=='i':
#         continue
#     print(letter)



#1-100 e kadar tek sayıların toplamı
x=1
toplam=0
while x<=100:
    x+=1
    if x%2==0:
        continue
    toplam+=x
    

print(f'toplam : {toplam}')