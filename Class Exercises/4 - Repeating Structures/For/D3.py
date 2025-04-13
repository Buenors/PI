#Soma multp 3 impares entre 1-500
soma = 0
for i in range (1,501,2): #percorre todos os impares
    if i % 3 == 0:
        soma += i
    
print(f'A soma dos múltiplos de 3 que são ímpares no intervalo(1-500) é: {soma}')
