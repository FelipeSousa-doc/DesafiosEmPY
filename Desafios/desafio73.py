'''
Faça um programa que mostre a tabuada de vários números, 
um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo.
'''
numero = 0
cont = 1

while True:
    numero = int(input("Quer ver a tabuada de qual número? "))
    cont = 1

    if numero > 0:
        while cont <=10:
            print(f'{numero}x{cont}={numero*cont}')
            cont += 1

    else:
        print("Dado inserido inválido, programa encerrado!")
        break
