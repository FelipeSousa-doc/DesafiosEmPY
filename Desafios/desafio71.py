''''
Crie um programa que leia números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
'''
c = 1
while True:
    print(f'{c} ->',end='')
    c += 1
    if c>=10:
        break

