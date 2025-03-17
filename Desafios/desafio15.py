"""
Faça um programa que leia o preço de um produto e mostre
seu novo preço com 5% de desconto.
"""
preco_produto = float(input("Digite o preço de um produto : R$"))
novo_preco_produto = preco_produto - (5 * preco_produto) / 100

print(f'O preço do produto era R${preco_produto:.2f} com desconto de 5% ficou R${novo_preco_produto:.2f}')