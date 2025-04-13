valores = []
print('para parar escreva "stop"')
while True:
    valor = str(input('Valor: '))
    if valor.upper() == 'STOP':
        break
    
    valor_num = int(valor)
    valores.append(valor_num)
    
listpar = []
listimpar = []
for n, valor in enumerate(valores):
    if valor%2 == 0:
        listpar.append(valor)
        
    else:
        listimpar.append(valor)
        
tam_impar = len(listimpar)
tam_par = len(listpar)

        
print(f'Os valores digitados são: {valores} \nOs {tam_par} par(es) digitados são: {listpar} \nOs {tam_impar} ímpar(es) digitados são:{listimpar}')