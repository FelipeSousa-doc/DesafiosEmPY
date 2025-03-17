"""
Faça um algoritmo que leia o salário de um funcionário
e mostre seu novo salário com 15% de aumento.
"""
salario_a = float(input("Digite o seu salário: R$"))
salario_novo = salario_a + (salario_a*15/100)

print(f'Seu salário era R${salario_a:.2F},\nnovo salário com 15% de aumento ficou R${salario_novo:.2F}.')
