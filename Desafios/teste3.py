soma = 0
numero = 0
c_n = 0

while numero != 999:
    numero = int(input("Digite um número [999 para parar o programa]: "))
    
    if numero == 999:
        soma -= 999
    
    soma += numero
    c_n += 1

print(f'Você digitou {c_n} e a soma deu {soma}')
