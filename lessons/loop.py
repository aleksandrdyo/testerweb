for x in range(0,10):
    print(x)

for x in range(0,20):
    print("count %s" % x)

wizard_list = ['паучьи лапки', 'жабий палец', 'язык улитки',
'крыло летучей мыши', 'жир слизня', 'медвежий коготь']

for x in wizard_list:
    print(x)
    print(1)


hugehairypants = ['огромные', 'волосатые', 'штаны']

for i in hugehairypants:
    print(i)
    for j in hugehairypants:
        print(j)

found_coins = 20
magic_coins = 70
stolen_coins = 3
coins = found_coins
for week in range(1, 53):
    coins = coins + magic_coins - stolen_coins
    print('Неделя %s = %s' % (week, coins))

x = 49
y = 90
while x < 50 and y < 100:
    x = x + 1
    y = y + 1
    print(x, y)

#1. Цикл с приветом
#Как вы считаете, что делает эта программа? Сперва придумайте вариант
#ответа, а потом запустите код и проверьте, угадали ли вы.
for x in range(0, 20):
    print('привет %s' % x)
    if x > 9:
        break
#2. Четные числа
#Создайте цикл, который печатает четные числа до тех пор, пока не выве-
#дет ваш возраст. Если ваш возраст —  нечетное число, создайте цикл, ко-
#торый печатает нечетные числа до совпадения с возрастом. Программа
#должна выводить на экран нечто подобное:
#2 4 6 8 10 12 14

for x in range (0,42,2):
    print(x)

#Создайте список с пятью разными ингредиентами для бутерброда, напо -
#добие:
ingredients = ['слизни', 'пиявки', 'катышки из пупка гориллы', 'брови гусеницы', 'пальцы многоножки']
#Теперь создайте цикл, который печатает список ингредиентов с нуме-
#рацией:wsdsadas


z=1
for x in ingredients:
    print(z, x)
    z = z + 1


#Ваш лунный вес
#Если бы вы сейчас были на Луне, ваш вес составил бы 16,5 процентов от
#земного. Чтобы узнать, сколько это, умножьте свой земной вес на 0,165.
#Если  бы  каждый  год  в  течение  следующих  15  лет  вы  прибавляли
#по одному килограмму веса, каким бы оказался ваш лунный вес в каж-
#дый из ежегодных визитов на Луну вплоть до 15-го года? Напишите про-
#грамму, которая с помощью цикла for печатает на экране ваш лунный
#вес в каждом году.

y=30
for x in range(1, 16):
    y = y + 1
    a = y * 0.165
    print("%s year is %s" % (x,a))
