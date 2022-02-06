bjj=['kimura', 'berimbolo', 'delariva', 'armbar', 'kneebar', 'amerikano']

bjj.append('spider')
bjj.append('omoplata')
bjj.extend(['qwe', 'asd'])
del bjj[0]

for x in bjj:
    print(x)

bjj1={'kimura', 'berimbolo', 'delariva', 'armbar', 'kneebar', 'amerikano'}

print(bjj1)

for x in bjj1:
    print(x)

myscore='5'
message = 'Мой счет: %s очков %s'
print(message % (1,2))

favorite_sports = {'Ральф Уильямс': 'Футбол',
'Майкл Типпетт': 'Баскетбол',
'Эдвард Элгар': 'Бейсбол',
'Ребекка Кларк': 'Нетбол',
'Этель Смит': 'Бадминтон',
'Фрэнк Бридж': 'Регби'}

for x in favorite_sports:
    print(favorite_sports[x])
