def testfunc(myname):
    print('Hello, %s' % myname)

testfunc("test")


def names(name, surname):
    print("hello mr %s %s" % (name, surname))

names('Alex', 'dyo')

def savings(pocket_money, paper_route, spending):
    return pocket_money + paper_route - spending

print(savings(5,5,9))


def variable_test():
    first_variable = 10
    second_variable = 20
    return first_variable * second_variable

print(variable_test())

another_variable = 100
def variable_test2():
    first_variable = 10
    second_variable = 20
    return first_variable * second_variable * another_variable

print(variable_test2())

def spaceship_building(cans):
    total_cans = 0
    for week in range(1, 53):
        total_cans = total_cans + cans
        print('Неделя %s, банок: %s' % (week, total_cans))

spaceship_building(2)

spaceship_building(5)