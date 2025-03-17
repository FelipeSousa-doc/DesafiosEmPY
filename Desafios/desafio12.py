"""
Faça um programa que leia um número inteiro qualquer
e mostre na tela sua tabuada.
"""
numero = int(input('Digite um número para ver sua tabuada: '))

cores = {'vermelhoen':'\033[31:1m','nenhum':'\033[m'}
print(f'A tabuada do {numero}:')
print('\033[1;33m-' * 20)
print(f'{cores['nenhum']}{numero}x 1 ={cores['vermelhoen']}{numero*1}{cores['nenhum']}')
print(f'{numero}x 2 ={cores['vermelhoen']}{numero*2}{cores['nenhum']}')
print(f'{numero}x 3 ={cores['vermelhoen']}{numero*3}{cores['nenhum']}')
print(f'{numero}x 4 ={cores['vermelhoen']}{numero*4}{cores['nenhum']}')
print(f'{numero}x 5 ={cores['vermelhoen']}{numero*5}{cores['nenhum']}')
print(f'{numero}x 6 ={cores['vermelhoen']}{numero*6}{cores['nenhum']}')
print(f'{numero}x 7 ={cores['vermelhoen']}{numero*7}{cores['nenhum']}')
print(f'{numero}x 8 ={cores['vermelhoen']}{numero*8}{cores['nenhum']}')
print(f'{numero}x 9 ={cores['vermelhoen']}{numero*9}{cores['nenhum']}')
print(f'{numero}x 10 ={cores['vermelhoen']}{numero*10}{cores['nenhum']}')
print('\033[33m-' * 20)