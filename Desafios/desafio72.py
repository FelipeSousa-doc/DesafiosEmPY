numero = 0
soma = 0
c = 0

while True:
    numero = int(input("Digite um valor [se quiser parar, digite '999']: "))

    if numero == 999:
        break

    else:
        c += 1
        soma += numero

print(f"Você digitou {c} valores  e a soma é {soma}.")