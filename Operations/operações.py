def soma(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b
    
def div_int(a,b):
    return a//b

def pot(a,b):
    return a**b

def med(a,b):
    return (a+b)/2

def cm(a):
#metros para centímetros
    return a*100

def mm(a):
#cm para mm
    return cm(a)*10

def desc(a,b):
    return a - (a*(b/100))

def tabuada(a,i):
    i = 0
    while i <= 10:
        t = a * i 
        print(f'{a}*{i}: {t}')
        i += 1
        return
    
       
    