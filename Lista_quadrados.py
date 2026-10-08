numeros = range(10)
quadrados = []
for num in numeros:
    quadrado = num**2 # equivale à fazer o quadrado de cada elemento da lista
    quadrados.append(quadrado) #adiciona os elementos na lista em si 

print(quadrados)

#também pode ser escrito:

quadrados = []
quadrados = [num**2 for num in numeros]

print(quadrados)