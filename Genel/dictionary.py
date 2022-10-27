#dictionary = map
#key - value
# 41 => kocaeli, 34=> istanbul

sehirler=['kocaeli', 'istanbul']
plakalar=[41,34]

print(plakalar[sehirler.index('kocaeli')])
print(plakalar[sehirler.index('istanbul')])

#bunun yerine
#print(plakalar['kocaeli']) => 41
#print(plakalar['istanbul']) => 34

plakalar={'kocaeli': 41, 'istanbul':34}
print(plakalar['kocaeli'])
print(plakalar['istanbul'])

plakalar['ankara']=6
plakalar['kocaeli']='new value'
print(plakalar)

users={
    'sadikturan':{
        'age':36,
        'roles': ['user'],
        'email':'sadik@gmail.com',
        'address' : 'kocaeli',
        'phone' : '1231321'
    },
    'çınarturan':{
        'age':2,
        'roles': ['admin', 'user'],
        'email':'cinar@gmail.com',
        'address' : 'kocaeli',
        'phone' : '1231321'
    }
}
print(users['çınarturan'])
print(users['çınarturan']['age'])
print(users['çınarturan']['email'])
print(users['çınarturan']['address'])
print(users['çınarturan']['phone'])
print(users['çınarturan']['roles'][0])