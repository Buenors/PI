v = int(input('Velocidade '))

m = (v - 80) * 7

if v > 80:
    print(f'Multado no valor de R${m:.2f}')