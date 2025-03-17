"""
Faça um programa que leia a largura e altura
de uma parede em m^2, calcule sua aré e a
quantidade de tinta necessária para pintá-la,
sabendo que cada L de tinta, pinta uma área de
2m^2
"""
largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))

area = largura * altura
litros = area/2

print(f"Sua parede tem dimensão de {largura}x{altura}, portanto {area}m².\nPortanto para pintar precisaria de \033[1m{litros:.2f}L\033[1m de tinta.")