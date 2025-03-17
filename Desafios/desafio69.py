n = 0
soma = 0
cont_n = 0
para = False
while para == False:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        n -= 999 
        para = True
        cont_n -= 1

    soma += n
    cont_n += 1 

print(f'Você digitou {cont_n} números. A soma entre eles deu {soma}.')
