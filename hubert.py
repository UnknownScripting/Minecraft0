
'''
def greet(name):
    print(f"Hello, {name}!")

greet("Adolph Blaine Charles David Earl Frederick Gerald Hubert Irvin John Kenneth Lloyd Martin Nero Oliver Paul Quincy Randolph Sherman Thomas Uncas Victor William Xerxes Yancy Zeus Wolfeschlegelsteinhausenbergerdorffwelchevoralternwarengewissenhaftschaferswessenschafewarenwohlgepflegeundsorgfaltigkeitbeschutzenvonangreifendurchihrraubgierigfeindewelchevoralternzwolftausendjahresvorandieerscheinenvanderersteerdemenschderraumschiffgebrauchlichtalsseinursprungvonkraftgestartseinlangefahrthinzwischensternartigraumaufdersuchenachdiesternwelchegehabtbewohnbarplanetenkreisedrehensichundwohinderneurassevonverstandigmenschlichkeitkonntefortpflanzenundsicherfreuenanlebenslanglichfreudeundruhemitnichteinfurchtvorangreifenvonandererintelligentgeschopfsvonhinzwischensternartigraum.")

def print_cube(number):
    print(f"The cube of {number} is {number ** 3}.")

print_cube(593148917027820483089895697973)


def add(a, b):
    print(f"The sum of {a} and {b} is {a + b}.")

add(79979987657598988767676767676676766767666656565656565656778987687656798767887698797678768767898767876787,3)


def power(x,y):
    print(f"{x} to the power of {y} is {x**y}.")

power(23,91)


def add_two_numbers(a, b):
    return a + b

result = add_two_numbers(234234,776979)
print(result)

def rock(word1,word2):
    return word1+word2+"rock"

result = rock("wow, that"," is a ")
print(result)

def plus_five(a, b) :
    a += 5
    b += 5
    return a, b

x, y = plus_five(3, 5)
print(x, y)
'''


from minecraft import *
import time
import random

def tree(x, y, z) :
    setblocks(x+2, y, z, x+4, y+a, z+2, 17)
    setblocks(x+1, y+a+1, z-1, x+5, y+a+1, z+3, 18)
    setblocks(x+2, y+a+2, z, x+4, y+a+2, z+2, 18)


for i in range(30):
    pos = getpos()
    x = pos.x
    y = pos.y
    z = pos.z
    a = random.randint(5, 80)
    tree(x, y, z)
    time.sleep(2)
    


