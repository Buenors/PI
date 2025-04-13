nome = str(input('Insira seu nome completo: ')).strip
separado = nome.split()
print(f'Primeiro nome: {separado[0]}. Último nome: {separado[-1]}')