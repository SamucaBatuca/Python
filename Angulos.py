from math import sin, cos, tan, radians

ang = float(input("Digite um ângulo qualquer: "))
ang = radians(ang)
print("Este é o seno: {:.2f}; cosseno: {:.2f}; tangente: {:.2f}".format(sin(ang), cos(ang), tan(ang)))