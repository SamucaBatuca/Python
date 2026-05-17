from math import hypot

co= float(input("Digite o cateto oposto: "))
ca= float(input("Digite o cateto adjacente: "))
print("A hipotenusa desse trinangulo é: {:.2f}" .format(hypot(co,ca)))