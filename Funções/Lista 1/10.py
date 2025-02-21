#Pedir dois numeros e exibir os resultados de comparações booleanas (>, <, ==, ! =).

n1 = float(input("Primeiro Número: "))
n2 = float(input("Segundo Número: "))

m1 = n1 > n2
m2 = n1 < n2
i = n1 == n2

print(f'Maior: {m1} \nMenor: {m2} \nIgual: {i} \nDiferente: {not(i)}')
