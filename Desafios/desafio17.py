"""
Escreva um programa que converta uma temperatura
digitada em ºC e converta para ºF.
"""
t_c = float(input('Digite a temperatura em ºC: '))
t_f = t_c * 1.8 + 32

print(f'{t_c:.2F}ºC corresponde a {t_f:.2F}ºF')
