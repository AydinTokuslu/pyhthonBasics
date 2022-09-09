
# def cube():
#     result=[]

#     for i in range(5):
#         result.append(i**3)
#     return result

# print(cube())

# from email import iterators


# def cube():
#     for i in range(5):
#             yield i ** 3  #yield, generator objesi
#generator, oluşturduğumuz elementi bir liste içinde kullanmamız, saklamamız gerekmiyorsa kullanırız.

# iterator=cube()

#iterator=iter(generator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for i in iterator:
#     print(i)


generator=(i**3 for i in range(5))
print(generator)

for i in generator:
    print(i)

# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))




