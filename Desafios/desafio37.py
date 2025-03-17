'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, 
calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''
salario = float(input('Digite seu salário R$'))
salario_novo = 0

if salario<= 1250:
    salario_novo =  salario + (salario * 15/100)
    print(F'Quem ganhava R${salario:.2F}, passa a ganhar R${salario_novo:.2F}.')

else:
    salario_novo = salario + (salario * 10/100)
    print(F'Quem ganhava R${salario:.2F},passa a ganhar R${salario_novo:.2F}')

print('BOM TRABALHO!')
