# print(type((4*5)/2)) / bölme tipi ve sonucu float olur
# print((4*5)//2)     // bölme tipi ve sonucu int olur
# a = (1+3) ** (2 ** (1*2/2)/2)
# print(a)           / bölme tipi ve sonucu float olur

print("True" and "False")
print(2 and "hello world")  # "hello world" döndürür
print(2 or "hello world")  # "hello world" döndürür
print("" and "hello world")  # boşluk döndürür
print(None and ())  # None döndürür
print({} or 0)  # F/F = F (or son değeri döndürür) 0 döndürür
print({0} or False)  # T/F = T   {0} döndürür
