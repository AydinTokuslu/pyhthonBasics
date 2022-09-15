import numpy as np

# numbers=np.array([0,5,10,15,20,25,50,75])

# result=numbers[5]
# result=numbers[5]
# result=numbers[0:3]
# result=numbers[:3]
# result=numbers[3:]
# result=numbers[::]# bütün listeyi getir.
# result=numbers[::-1]# bütün listeyi tersten getir.

# numbers2=np.array([[0,5,10],[15,20,25],[50,75,85]])
# print(numbers2)
# result=numbers2[0] # [0,5,10]
# result=numbers2[2] # [50,75,85]
# result=numbers2[0,2] # 10
# result=numbers2[:,2] # : bütün satırları seçmek demek, [10,25,85]
# result=numbers2[:,0:2] # : bütün satırlardan 0 ve 2nci indexi seçmek
# result=numbers2[-1,:]
# result=numbers2[:2,:2]

# print(result)

arr1=np.arange(0,10)
#arr2=arr1 # referans kopyalaması
arr2=arr1.copy() #sadece kopyalar, index değişikliği etkilemez.

arr2[0]=20 # her ikisinde de 0 index 20 olur

print(arr1)
print(arr2)