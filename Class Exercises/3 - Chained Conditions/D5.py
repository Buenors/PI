s = float(input('Sálario do funcionário: '))

if s > 1518:
    a = s * (1+0.1)
    print(f'Sálario com aumento 10% R${a:.2f}')
    
else:
    a = s * (1+0.15)
    print(f'Sálario com aumento de 15% R${a:.2f}')