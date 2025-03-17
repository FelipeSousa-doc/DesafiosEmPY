import time
"""
Crie um algoritmo que leia o número e mostre o seu dobro, triplo e
a raiz quadrada.
"""
numero = int(input('Digite um número: '))

dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

print('\033[1;35;43mPROCESSANDO...\033[m')
time.sleep(1)
print(f' O dobro de {numero} é \033[4m{dobro}\033[m \n O triplo de {numero} é \033[4m{triplo}\033[m \n A raiz de {numero} é \033[4m{raiz:.2f}\033[m.')

