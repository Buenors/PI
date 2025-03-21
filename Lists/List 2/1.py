n = int(input('Número de partidas: '))
soma = 0
for i in range (n):
    x = int(input('Diferença de pontos da Maria: '))
    
    if x > 0:
        if x <144:
            print('Ganhou 88 reais')
            soma += 88
        else:
            print('Ganhou 176 reais')
            soma +=176
            
    elif x == 0:
        print('Empate')
    
    else:
        if x <= -144:
            print('Perdeu 176 reais')
            soma -= 176
        else:
            print('Perdeu 88 reais')
            soma -= 88

print('Saldo final R${soma},00')