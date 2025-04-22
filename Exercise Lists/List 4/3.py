valores = list()
while True:
    x = str(input(f'Insira os valores, para parar digite "stop": '))
    if x.lower() == 'stop':
        break
    valores_num = int(x)
    valores.append(valores_num)
        
valores.sort(reverse=True)
tamanho = len(valores)

if 5 in valores:
    x = 'está'
else:
    x = 'não está'
        
print(f'\nForam digitados {tamanho} números \nA lista em ordem decrescente é {valores}\nO número 5 {x} na lista')