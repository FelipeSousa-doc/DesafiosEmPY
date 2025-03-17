'''
Crie um programa que leia o nome completo de uma pessoa e mostre: 
O nome com todas as letras maiúsculas e minúsculas.
Quantas letras ao todo (sem considerar espaços).
Quantas letras tem o primeiro nome.
'''
nome = str(input('Digite seu nome completo: '))
sem_es = nome.split()

print(f"""O nome digitado foi {nome.strip()}:
Todo maiusculo: {nome.strip().upper()}
Todo minusculo: {nome.strip().lower()}
Quantas letras tem: {len(''.join(sem_es))}
Quantas letras tem o primeiro nome {len(sem_es[0])}
Quantas letras tem o ultimo nome {len(sem_es[-1])}""")
