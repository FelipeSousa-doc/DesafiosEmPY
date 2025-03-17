"""
Crie um programa que leia um número Real qualquer
pelo teclado e mostre na tela sua posição inteira.
"""
from math import floor
numero = float(input('Digite um número: '))
numero_int = (floor(numero))

print(f'O número {numero} tem a parte inteira {numero_int}')
