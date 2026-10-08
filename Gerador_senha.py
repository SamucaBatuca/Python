import random

def senha (tam):
    sen = str()
    digitos = "123456789ABCD"
    for i in range(tam):
        sen = sen + random.choice(digitos)
    return sen
    
a = senha(7)
print(a)