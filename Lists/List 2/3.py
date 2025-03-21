A = int(input('valor do dado de Alice: '))
B = int(input('valor do dado de Bob: '))
E = int(input('valor do dado de Eva: '))

if A > B and E:
    print('Alice venceu')

elif B > A and E:
    print('Bob venceu')
    
elif E > A and B:
    print('Eva venceu')

elif A == B or A == E or B == E:
    print('Empate')