"""
Crie um script Python que leia dois números e tente
mostrar a soma entre eles.
"""

print('\033[33m-' * 40)
print('          DESAFIO 03      ')
print('\033[33m-' * 40,'\033[m')

primeiro_numero = int(input('Primeiro número: '))
segundo_numero = int(input('Segundo número: '))
soma = primeiro_numero + segundo_numero

print(f'A soma entre {primeiro_numero} e {segundo_numero} é \033[1:34m{soma}\033[m.')
