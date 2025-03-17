soma = 0
cont = 0

for c in range(1,7):
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        soma += numero
        cont += 1

if soma == 0:
    print('Você não digitou nenhum número par.')

print(f'Você me informou {cont} números pares,a soma dos número pares foi \033[1m{soma}.')