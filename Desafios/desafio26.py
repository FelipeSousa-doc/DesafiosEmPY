'''
 Faça um programa que leia um número de 0 a 9999 
 e mostre na tela cada um dos dígitos separados.

'''
casas = '000'
numero = str(input('Digite um número: '))
junto = casas + numero
print(F"""A unidade é: {junto[-1]}
A dezena é: {junto[-2]}
A centena: {junto[-3]}
A unidade de milhar: {junto[-4]} 
""")