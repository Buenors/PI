s = input('Salário a ser alterado:')
p = float(input('Porcentagem: '))

s_alt = s * (1 + p/100)

print(f'O salário de R${s:.2f} após um aumento de {p}% é igual a: R${s_alt:.2f}')