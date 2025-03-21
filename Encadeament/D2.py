#Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai
#perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da
#prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

v = float(input('Valor da casa: '))
s = float(input('Sálario: '))
p = int(input('Anos para pagar: '))
m = v / (p * 12)
d = s*0.3

if d >= m:
    print(f'Aprovado o valor da mensalidade é {m}')
    
else:
    print('Negado')
