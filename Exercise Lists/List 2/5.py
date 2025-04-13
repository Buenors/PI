a = float(input('Insira o primeiro número do intervalo: '))
b = float(input('Insira o segundo número do intervalo: '))
if a > b:
    print('O primeiro numero deve ser menor que o segundo')



    
else:
    x = float(input('Insira o número a verificar se está dentro do limite: '))
    if a <= x and x <= b:
        print(f'{x} está dentro do intervalo [{a,b}]')
    else:
        print(f'{x} está fora do intervalo [{a,b}]')
        
