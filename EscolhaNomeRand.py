from random import choice, shuffle

a1 = str(input("Primeiro aluno: "))
a2 = str(input("Segundo aluno: "))
a3 = str(input("Terceiro aluno: "))
a4 = str(input("Quarto aluno: "))

lista = [a1,a2,a3,a4];

print("O aluno escolhido foi: {}".format(choice(lista)))
shuffle(lista)
print("Agora, vou embaralhar e vai ficar assim: {}".format(lista))