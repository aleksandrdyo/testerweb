#import time
import sys

#a = time.asctime()

#print(sys.stdin.readline())

#def silly_age_joke(age):
#    if age >= 10 and age <= 13:
#        print('13 + 49 + 84 + 155 + 97: что получится? Головная боль!')
#    else:
#        print('Что-что?')

#silly_age_joke(1)

def silly_age_joke():
    print("How old is you?")
    age=int(sys.stdin.readline())
    if age >= 10 and age <= 13:
        print('13 + 49 + 84 + 155 + 97: что получится? Головная боль!')
    else:
        print('Что-что?')

#silly_age_joke()

#1. Функция лунного веса
#Одним из заданий к главе 6 было создание цикла for для
#расчета вашего веса на Луне в течение 15 лет. Этот цикл
#можно оформить в виде функции. Создайте функцию, ко-
#торая принимает начальный вес и величину, на которую
#вес увеличивается каждый год. Вызывать эту новую функ-
#цию нужно будет примерно так:
#>>> moon_weight(30, 0.25)

#def moon_weight(weight,increase, year):#
#    for x in range(1,year+1):
#        weight=weight+increase
#        a=weight*0.165
#        print("%s year, weight is %s" % (x, a))

#moon_weight(40, 0.5, 15)



def moon_weight():
    print("Введите количество лет")
    year = int(sys.stdin.readline())
    print("Введите ваш нынешний земной вес")
    weight = int(sys.stdin.readline())
    print("Введите ежегодный прирост вашего веса")
    increase = float(sys.stdin.readline())
    for x in range(1,year+1):
        weight=weight+increase
        a=weight*0.165
        print("%s year, weight is %s" % (x, a))

moon_weight()
