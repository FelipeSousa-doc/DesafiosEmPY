'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

resposta = 'l'
cont_num = 0
maior = 0
menor = 0
teste = 0
soma = 0

while resposta != 'n':
    numero = float(input('Digite um número: '))
    cont_num += 1
    soma += numero

    if teste == 0:
        teste += 1
        menor = numero
        maior = numero
    
    elif numero < menor:
        menor = numero
    
    elif numero > maior:
        maior = numero

    resposta = input('Quer continuar?[S/N] ').lower().strip()

media = soma/cont_num

print(f'Você digitou {cont_num} números.\nO maior valor foi {maior} e o menor valor foi {menor}.\nA média entre eles é {media:.1f}.')
