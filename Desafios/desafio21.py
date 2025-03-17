"""
Faça um programa que leia um ângulo qualquer e
mostre na tela o valor do seno, cosseno e tangente desse
ângulo.
"""
from math import radians, cos, tan, sin
angulo = float(input('Digite o angulo: '))
radiano = radians(angulo)
coss = cos(radiano)
tang = tan(radiano)
sen = sin(radiano)

print(f'O angulo de {angulo} graus tem: \n'
      f'O seno de {sen:.2F}\n'
      f'O cosseno de {coss:.2F}\n'
      f'A tangente de {tang:.2F}')



