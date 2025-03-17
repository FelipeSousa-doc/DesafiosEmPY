"""
Crie um script Python que leia o dia, o mês e o ano de nascimento
de uma pessoa e mostre uma mensagem com a data formatada.
"""
dia = input('Qual dia você nasceu? ')
mes = input('Qual mês você nasceu? ')
ano = input('Qual ano você nasceu? ')

print('Você nasceu no dia \033[1m', dia, '\033[m de \033[1m', mes,'\033[m de \033[m \033[1m', ano + '\033[m.','Correto?')