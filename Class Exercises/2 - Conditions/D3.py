#Considere que uma disciplina tem o seguinte critério de aprovação: média simples das provas ≥ 50 e presença ≥ 75.
#Faça um programa que: recebe a nota da P1 (um número real); recebe a nota da P2 (um nu ́mero real); recebe a
#presença (um número real); calcula a média e de acordo com o critério de aprovação definido, imprime “S” se
#passou e “N” se não passou.

n1 = float(input('Nota 1: ' ))
n2 = float(input('Nota 2: ' ))
p = float(input('Presença em %: ' ))
m = (n1+n2)/2

if p >= 75 and m >=50:

        print('Aprovado')
        
else:
    print('Reprovado')