print('Ola mundo')
print(7+4)
print('Numero texto', 5)
# comentário
'''
muito comentado
'''
print('='*20)  # da pra fazer isso tbm
nome = 'Nomeado'
print(nome)
idade = input("Fala tua idade: ")
print(idade)

print("É assim que printa formatado: {} e {}. Tendeu?!".format(nome,idade))
print('='*20)

print(type(idade))  #sempre é string se n tipar

d = int(idade)      # converte de string para int
print(type(d))

d = d%2
print(d)
print('='*20)
n =  input('Digita algo ai: ')
if n.isnumeric():
    print('Da pra converter pra int')
else:
    print('N da pra converter pra int')
print("Da pra ver mais coisa do N como: {}, {}, {}, {}, {}, {}"
        .format(n.isspace(), n.isalpha(), 
                n.isdecimal(), n.isascii(), 
                n.isprintable(), n.istitle())) 
# "title" é para ver se está com letras maiúsculas e minúsculas, ou se alternam 
# entre letras e números
print('='*20)
aux = int 
'''
isso não torna aux do tipo inteiro. Isso 
define aux como sendo um apelido para inteiro
'''
print(aux)
print('='*20)
aux = float(5.5) # aqui ele é definido como tipo float
m = aux // 2     # aqui foi feita a divisão inteira que conservou o tipo float (por mais que M seja string)
print(m)
print('='*20)

print('Assim eu alinho à direita vinte espaços : {:>20}'.format(nome))
print('Assim eu alinho à esquerda vinte espaços: {:<20}'.format(nome))
print('Assim eu alinho no meio vinte espaços   : {:^20}'.format(nome)) #esse aqui alinha mais ou menos no meio
print('Da pra preencher o alinhamento tbm      : {:=^20}'.format(nome)) 
print('Casa flutuante eh assim: {:.3f}'.format(4/3))
print('Assim quebra a linha \nAssim junta', end=' ')
print('Dois prints. E assim eu mudo oq tem no ', end='>final<\n')

print('='*20)





