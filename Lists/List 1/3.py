# Tinta-Parede

l = float(input("Largura da parede: "))
h = float(input("Altura da parede: "))

A = l*h

#Cada lata pinta 2 metros quadrados

import math
T = math.ceil(A/2)

print(f'Largura: {l}m \nAltura: {h}m\u00b2 \nÁrea: {A}m \nLatas necessárias: {T} Latas')
#\u2082 subescrito 2
#\u00b2 sobrescrito 2