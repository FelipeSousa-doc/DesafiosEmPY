from time import sleep

primeiro_valor = int(input('Primeiro valor: '))
segundo_valor = int(input('Segundo valor: '))

soma = 0
opcao = ''
acabou = False

while not acabou:
    print('''O que você quer fazer?
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa
''')
    
    opcao = int(input('Digite uma opção: '))
    if opcao == 5:
        acabou = True

    elif opcao == 1:
        soma = primeiro_valor + segundo_valor
        print(f'A soma entre {primeiro_valor} e {segundo_valor} é {soma}.')

    elif opcao == 2:
        multiplicacao = primeiro_valor * segundo_valor
        print(f'A multiplicação entre {primeiro_valor} e {segundo_valor} é {multiplicacao}.')

    elif opcao == 3:
        if primeiro_valor > segundo_valor:
            print(f'O maior entre {primeiro_valor} e {segundo_valor} é {primeiro_valor}.')

        elif segundo_valor > primeiro_valor:
            print(f'O maior entre {primeiro_valor} e {segundo_valor} é {segundo_valor}.')
            print('-*' * 15)
        else:
            print(f'Os valores {primeiro_valor} e {segundo_valor} são iguais.')
    
    elif opcao == 4:
        primeiro_valor = int(input('Primeiro valor: '))
        segundo_valor = int(input('Segundo valor: '))
    else:
        print('Opção invalida!. Tente novamente! ')
    print('-*' * 15)
    
print('\033[1;35mFinalizando...\033[m')
sleep(1)

print('FIM DO PROGRAMA! VOLTE SEMPRE!')
