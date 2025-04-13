tabela = list()
dado = list()
n = int(input('Numero de alunos: '))
for c in range(0, n):
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Idade: ')))
    dado.append(float(input('Idade: ')))
    media = dado.append((dado[2]+dado[1])/2)
    tabela.append(f'{media:.2f}')
    dado.clear()
    
print('Nome','Nota 1', 'Nota 2', 'Média')

for p in tabela:
    print(p[0],p[1],p[2],p[3])