numero = int(input('Digite um número: '))
contador = numero 
fac = 1

print(f'{numero}! =',end=' ')

while contador > 1:
    print(f'{contador} x ',end='')
    contador -= 1
    fac *= (numero * contador)
    numero = 1
print('1 = ',end='')
print(f'{fac}')