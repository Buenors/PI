galera = list()
dado = list()
maior = menor = 0

for c in range(0, 5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[ : ])
    dado.clear()


for p in galera:
    if p[1] >= 21:
        maior += 1

        
    else:
        menor += 1

        
print(galera)
print(maior)
print(menor)