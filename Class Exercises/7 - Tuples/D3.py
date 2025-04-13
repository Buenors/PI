a = int(input('Primeiro Número: '))
b = int(input('Segundo Número: '))
c = int(input('Terceiro Número: '))
d = int(input('Quarto Número: '))
e = int(input('Quinto Número: '))

num = (a ,b ,c ,d, e)
num_org = sorted(num)

print(f'O menor valor é {num_org[0]} o maior é {num_org[4]}')
