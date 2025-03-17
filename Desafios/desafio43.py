import datetime

sexo = str(input('Qual o seu sexo?[M]/[F]: ')).upper()
ano = int(input('Digite o ano do seu nascimento: '))
ano_a = datetime.datetime.now().year
idade = ano_a - ano

if sexo == 'F':
    print(f'O alistamento não é obrigatório para Mulheres!')

elif idade == 18:
    print(F'Quem nasceu em {ano} tem {idade} anos em {ano_a}.\n\033[1;32mSe aliste AGORA!')

elif idade < 18:
    print(F'Quem nasceu em {ano} tem {idade} ano(s) em {ano_a}.'
          F' Faltam {18-idade} anos para alistar. \033[1;33mSerá em {(18-idade)+ano_a}.')
    
else:
    print(F'Quem nasceu em {ano} tem {idade} anos em {ano_a}.'
          F' Você deveria ter se alistado {idade-18} anos atrás. \033[1;31mSeu alistamento foi em {ano_a - (idade-18)}.')
