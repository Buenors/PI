d = float(input('Distância da viagem em km: '))

if d <= 200:
    p = 0.5 * d
    print(f'A passagem custa R${p:.2f}')
    
else: 
    p =0.45 * d
    print(f'A passagem custa R${p:.2f}') 