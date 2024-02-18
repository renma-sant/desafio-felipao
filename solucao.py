nick = input('Insira o seu nickname: ')
xp = int(input('Insira a quantidade de experência do seu heroi: '))

if xp <= 1000:
    nivel = 'Ferro'
elif xp < 2001:
    nivel = 'Bronze'
elif xp < 5001:
    nivel = 'Prata'
elif xp < 7001:
    nivel = 'Ouro'
elif xp < 8001:
    nivel = 'Platina'
elif xp < 9001:
    nivel = 'Ascendente'
elif xp < 10001:
    nivel = 'Imortal'
else:
    nivel = 'Radiante'


print('O Herói de nome {} está no nível de {}.'.format(nick, nivel))