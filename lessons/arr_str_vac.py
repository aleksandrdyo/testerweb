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


money = 2000
if money > 1000:
    print("Я богат!")
else:
    print("Я не богат!")
    print("Может, когда-нибудь потом…")


#2. Бисквитики!
#Создайте конструкцию if, которая проверяет, действительно ли коли-
#чество бисквитов (которое задано в переменной twinkies) меньше 100
#или больше 500. Если это условие выполняется, пусть ваша программа
#напечатает сообщение «Слишком мало или слишком много».

twinkies=501

if twinkies < 100:
    print("to low")
elif twinkies > 500:
    print("to much")
else:
    print("normal")

#3. Подходящая сумма
#Создайте конструкцию if, которая проверяет, соответствует ли задан-
#ная в переменной money сумма денег диапазону значений от 100 до 500
#или диапазону значений от 1000 до 5000.
money=4999
if money > 100 and money < 500:
    print("not much")
elif money > 1000 and money < 5000:
    print("to much")
elif money < 100:
    print("to low")
else:
    print("normal")



#4. Я одолею этих ниндзя!
#Создайте конструкцию if, которая печатает строку «Их слишком мно-
#го», если количество ниндзя (заданное в переменной ninjas) меньше 50,
#печатает «Будет непросто, но я с ними разделаюсь», если это количество
#меньше 30, и печатает «Я одолею этих ниндзя!», если количество мень-
#ше 10. Проверьте, как ваш код работает с таким значением:

ninjas=51

if ninjas < 50:
    print("Их слишком много")
elif ninjas < 30:
    print("Будет непросто, но я с ними разделаюсь")
elif ninjas < 10:
    print("Я одолею этих ниндзя!")
else:
    print("very much")