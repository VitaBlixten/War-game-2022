from cmu_graphics import *

Trees = Group()
def TreeTop():
    for i in range(21):
        tt = 10 + 20*i
        Circle(10, tt, 10, fill="green", border='black', borderWidth=1)
        Circle(390, tt, 10, fill="green", border='black', borderWidth=1)
        Circle(tt, 10, 10, fill="green", border='black', borderWidth=1)
        Circle(tt, 390, 10, fill="green", border='black', borderWidth=1)

TreeTop()