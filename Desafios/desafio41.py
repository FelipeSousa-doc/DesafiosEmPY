import time

numero = int(input('Digite um número INTEIRO:'))

print('Escolha para o que quer converter: \n\033[1;31m[1]\033[m converter para BINÁRIO\n\033[1;31m[2]\033[mConverter para OCTAL'
      '\n\033[1;31m[3]\033[m converter para HEXADECIMAL')

op = int(input('Sua escolha: '))

print('\033[1;35mProcessando...\033[m')
time.sleep(1.2)

if op == 1:
    print(f'O número {numero} em binário é \033[1;34m{bin(numero).replace('0b','')}\033[m.')

elif op == 2:
    print(F'O número {numero} em OCTAL é \033[1;34m{oct(numero).replace('0o','')}.\033[m')

elif op == 3:
    print(F'O número {numero} em HEXADECIMAL é \033[1;34m{hex(numero).replace('0x','')}.\033[m')
    
else:
    print('A opção escolhida não é válida!')

