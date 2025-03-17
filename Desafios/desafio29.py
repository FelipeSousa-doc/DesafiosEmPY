'''
 Faça um programa que leia uma frase pelo teclado 
 e mostre quantas vezes aparece a letra "A", 
 em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''

frase = str(input('Digite uma frase: ')).strip()
fraselo = frase.lower()
fraselosplit = fraselo.split()

print(f'''A letra A aparece {fraselo.count('a')} vezes na frase.
A primeira letra A apareceu na posição {fraselo.find('a')+1}
A última letra A apareceu na posição: {fraselo.rfind('a')+1}
''')
