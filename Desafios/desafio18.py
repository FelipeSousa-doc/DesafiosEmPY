"""
Escreva um programa que pergunte a quantidade de KM
percorridos por um carro alugado e a quantidade de dias
pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$60 por dia e R$0.15 por KM
rodado.
"""
km = float(input("Quantos km rodados? "))
dias = int(input("Quantos dias? "))
valor_a_pagar = (60 * dias) + (0.15 * km)

print(f'O valor a pagar é R${valor_a_pagar:.2F}')
