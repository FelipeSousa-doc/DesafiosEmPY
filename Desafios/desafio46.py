import emoji

p_s = float(input('Digite o primeiro segmento: '))
s_s = float(input('Digite o segundo segmento: '))
t_s = float(input('Digite o terceiro segmento: '))

pode_f = p_s < s_s + t_s and s_s < p_s + t_s and t_s < s_s + p_s

if pode_f == False:
    print(emoji.emojize('NÃO PODE FORMAR UM TRIANGULO! 😔'))

elif p_s == s_s and t_s == s_s:
    print(emoji.emojize('Pode formar um triângulo EQUILATÉRO! 🔺'))

elif p_s != s_s and p_s != t_s and t_s != p_s and t_s != s_s:
    print(emoji.emojize('Pode formar um triângulo ESCALENO! 🔺'))

else:
    print(emoji.emojize('Pode formar um triângulo ISÓSCELES! 🔺'))
