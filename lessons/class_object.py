class Things:
    pass

class Inanimate(Things):
    pass

class Animate(Things):
    pass

class Sidewalks(Inanimate):
    pass

class Animals(Animate):
# Аргумент self дает функции класса возможность вызывать другие функции этого класса (а также классов-предков)
    def breathe(self):
        print("дышет")
    def move(self):
        print("двигается")
    def eat_food(self):
        print("ест")

class Mammals(Animals):
    def feed_young_with_milk(self):
        print("кормит детей молоком")

class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print("ест листья с деревьев")

reginald=Giraffes() # создать объект класса Giraffes и присвоить его переменной reginald.
reginald.move()
reginald.eat_leaves_from_trees()

harold = Giraffes()
harold.move()


class ThisIsMySillyClass:
    def this_is_a_class_function():
        print('Я – функция класса')
    def this_is_also_a_class_function():
        print('Я тоже функция класса, понятно?')

