nome = str(input('Insira seu nome: ')).strip
separado = nome.split()
letras = len(separado[0])
print(f'O seu primeiro nome ({separado[0]}) tem {letras} letras')
