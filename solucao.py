''' Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

Se XP for menor do que 1.000 = Ferro
Se XP for entre 1.001 e 2.000 = Bronze
Se XP for entre 2.001 e 5.000 = Prata
Se XP for entre 5.001 e 7.000 = Ouro
Se XP for entre 7.001 e 8.000 = Platina
Se XP for entre 8.001 e 9.000 = Ascendente
Se XP for entre 9.001 e 10.000= Imortal
Se XP for maior ou igual a 10.001 = Radiante

## Saída

Ao final deve se exibir uma mensagem:
"O Herói de nome **{nome}** está no nível de **{nivel}**" '''

# nick = input('Insira o seu nickname: ')
nick = 'renma'
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