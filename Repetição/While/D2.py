n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))

while True:
    print(f'Escolha uma operação:\n->(1) Soma \n->(2) Multiplicação \n->(3) Maior que \n->(4) Escolher novos números \n->(5) Sair')
    menu = int(input('Operação: '))
    if menu == 1:
        print(f'n1+n2 = {n1+n2}')
        
    if menu == 2:
        print(f'n1*n2 = {n1*n2}')
        
    if menu == 3:
        if n1>n2:
            print('É maior')
        else:
            print('Não é maior')
        
    if menu == 4:
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
        
    if menu == 5:
        print('Fim')
        break