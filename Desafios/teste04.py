num = 0 #variavel que eu vou usar la embaixo (todas essas)
opcao = ''
num_c = 0
soma_num = 0
maior = 0
menor = 0

while opcao != 'n': #enquanto a opcao que o usuario escolher for diferente de 'n', esse comando inteiiro vai executar
    
    try: #tente
        num = float(input('Digite um número: '))
        soma_num += num #quero somar os números
        num_c += 1 #contar quantos números são

        if num_c == 1: #se o num_c for igual a 1 (primeiro numero digitado), ele vai ser o maior e menor número (que assim eu consigo testar os outros)
            maior = num 
            menor = num

        elif num > maior: #se o numero digitado for maior que o maior(anterior)
            maior = num

        elif num < menor: #mesma coisa pro menor
            menor = num

        opcao = str(input('Quer continuar? [S/N]: ')).lower() #aqui eu pergunto se o usuario quer mais numero
    
    except: #exceto (se o usuario digitar algo errado!!!)
        print('Invalido! tente novamente.')

media = soma_num/num_c #aqui eu tiro a media dos numeros

print(f'Você digitou {num_c:.0f} números;\nA média foi {media:.1f};\nO maior número foi {maior:.0f} e o menor número foi {menor:.0f}')
