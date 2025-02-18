import operações as op
a = float(input("A "))
b = float(input("B "))

s = op.soma (a,b)
m = op.mult (a,b)
d = op.div (a,b)
di = op.div_int (a,b)
po = op.pot(a,b)
print(f' A soma é {s} \nA multiplicação é {m} \nA divisão é {d:.3f}\nA divisão inteira é {di} \n A potenciação é {po} ')
