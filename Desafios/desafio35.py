'''
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

'''
import datetime
from calendar import isleap

ano = int(input('Digite o ano, se quiser analisar o atual, digite "0": '))

if ano == 0:
    ano = datetime.date.today().year

if isleap(ano):
    print('O ano {} é BISSEXTO.'.format(ano))
    
else:
    print('O ano {} não é BISSEXTO.'.format(ano))

