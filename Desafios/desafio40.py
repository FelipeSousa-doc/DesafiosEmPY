'''
 Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
 Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
 A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''
casa = float(input('Valor da casa: '))

salario = float(input('Qual seu salário? '))

anos = int(input('Quantos anos de financiamento? '))

prestacao = casa/(12*anos)

calculo = salario*30/100

if prestacao >= calculo:
    print(F'Para pagar uma casa de R${casa:.2F}, no periodo de {anos} anos com parcelas de R${prestacao:.2F} empréstimo pode ser NEGADO')

elif prestacao < calculo:
    print(F'Para pagar uma casa de R${casa:.2F}, no periodo de {anos} anos com parcelas de R${prestacao:.2F},empréstimo pode ser CONCEDIDO')

