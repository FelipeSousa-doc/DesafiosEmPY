soma = 0
q_n = 0

for c in range (1,501, 2):
    if c%3 == 0:
        q_n = q_n + 1
        soma += c

print(f'a soma dos {q_n} valores é {soma}')
