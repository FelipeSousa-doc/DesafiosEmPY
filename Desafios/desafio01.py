"""    Crie um script Python que leia o nome de uma pessoa
e mostre uma mensagem de boas-vindas de acordo com o valor digitado."""

nome = input('Qual é o seu nome? ')

print('-' * 20)
print(f'  {'\033[1:32:44m'}DESAFIO 02\033[m            ')
print('Olá \033[1:35m', nome,'\033[m! é um prazer te conhecer!')
