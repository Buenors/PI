def saudacao():
    print('Hello, world!')
    
def dobro():
    n = input('Insira o numero: ')
    print(f'o dobro de {n} é {n*2}')
    
def area():
    l = input('Largura: ')
    h = input('Altura: ')
    a = l*h
    print(f'A área do retângulo {l}x{h} é: {a}')
    
def contador(i,f,p):
    from time import sleep

    for x in range (i, f+1, p):
        print(x)
        sleep(p)


    for x in range (f+1,1,-p*2):
        print(x-1)
        sleep(p*2)
    
    
def area_circulo():
    from math import pi
    r = float(input('Raio do círculo: '))
    a = pi * r**2
    print(f'A área do círculo de raio {r} é: {a}')
        