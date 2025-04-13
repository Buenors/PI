import random as rd

numeros = tuple(rd.randint(0,10) for i in range(0,5))
maior = max(numeros) 
menor = min(numeros)
     
print(f'Os números gerados são: {numeros} \nO maior é: {maior} \nO menor é: {menor}')

