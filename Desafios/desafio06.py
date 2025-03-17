"""
Faça um programa que leia algo pelo teclado e mostre na
tela o seu tipo primitivo e todas as informações possíveis
sobre ele.
"""
cores = {'nenhum':'\033[m',
         'negrito':'\033[1m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'ciano':'\033[36m',}

print('\033[1m-='*20)
print('\033[1mTIPOS PRIMITIVOS')
print('\033[1m-='*20)
algo = input('\033[mDigite algo: ')

print(f'O tipo primitivo é: {cores['negrito']}',type(algo))
print(f'{cores['nenhum']}Só tem espaços? {cores['negrito']}{cores['verde']}',algo.isspace())
print(f'{cores['nenhum']}É um número? {cores['negrito']}{cores['vermelho']}',algo.isnumeric())
print(f'{cores['nenhum']}É alfabético? {cores['negrito']}{cores['azul']}',algo.isalpha())
print(f'{cores['nenhum']}Está em maiúsculas? {cores['negrito']}{cores['amarelo']}',algo.isupper())
print(f'{cores['nenhum']}Está em minúsculas? {cores['negrito']}{cores['roxo']}',algo.islower())
print(f'{cores['nenhum']}Está capitalizada? {cores['negrito']}{cores['ciano']}',algo.istitle())

