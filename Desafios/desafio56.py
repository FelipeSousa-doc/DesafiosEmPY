num = int(input('Digite um número: '))
div = 0

for c in range(1,num+1):
    if num % c == 0:
        print(f'\033[32m{c}\033[m', end=' ')
        div += 1
    elif num % c != 0:
        print(F'\033[31m{c}\033[m', end =' ')
print(F'\nO número foi dividido {div} vezes.')
if div == 2:
    print('O número é PRIMO!')
elif div !=2:
    print('O número NÃO É PRIMO!')
