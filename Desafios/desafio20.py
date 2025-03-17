"""
Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo retângulo, calcule
e mostre o comprimento da hipotenusa.
"""

"""
cateto_oposto = float(input('Qual o cateto oposto? '))
cateto_adjacente = float(input('Qual o cateto adjacente? '))

hip = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)

print(f'A hipotenusa é {hip}')
"""
from math import hypot

cateto_oposto = float(input('Qual o cateto oposto? '))
cateto_adjacente = float(input('Qual o cateto adjacente? '))
hip = hypot(cateto_oposto, cateto_adjacente)

print(f'O comprimento da hipotenusa é {hip:.2F}')
