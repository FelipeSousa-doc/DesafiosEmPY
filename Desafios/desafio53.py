numero = int(input('Digite o número e veja sua tabuada: '))
for c in range(1,11):
    print(f'\033[1m{numero} x {c} = \033[1;35m{numero * c}\033[m')
