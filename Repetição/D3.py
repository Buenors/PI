#Soma multp 3 entre 1-500
soma = 0
for i in range (1,501,):
    if i % 3 == 0:
        soma += i
    
print(f'A soma dos múltiplos de 3 no intervalo(1-500) é: {soma}')
