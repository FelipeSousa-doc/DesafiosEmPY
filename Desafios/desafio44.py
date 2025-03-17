nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2

print(f'Sua média é \033[1;35m{media:.2F}\033[m.')

if media <5:
    print('Você está \033[1;31mREPROVADO!')

elif media >=5 and media <7:
    print('Você está de \033[1;33mRECUPERAÇÃO!')
    
elif media >=7:
    print('Você está \033[1;32mAPROVADO!')
