from cmu_graphics import *
from sys import exit

Options = Image('Installningar.png',0,0,height=400,width=400,visible = False)
back1 = Rect(20,347,85,33,fill=rgb(72,76,67), border='Black',visible = False)
yes = Label('Back',63,363,size=25,fill=rgb(228,224,210),visible = False)

###Box
back = Image('Startsida.png',0,0,height=400,width=400)
box = Rect(148,197,105,43,fill=None, border='Black')
plus1 = Rect(148,148,105,43,fill=None, border='Black')
plus2 = Rect(148,296,105,43,fill=None, border='Black')
plus3 = Rect(148,249,105,43,fill=None, border='Black')


Pic = Group(

)

boxes = Group(
back,
box, 
plus1, 
plus2,
plus3, 
)


def help():
    controls = "To move your troops:"
    controlss = "Click on the troop you want to move"
    controlsss = "and click on a empty tile" 
    controls1 = "To attack enemy troops:" 
    controlss1 = "Click on the troop you want to attack with" 
    controlssss1 = "and click on an enemy troop with a range" 
    controlsss1 = "of x to shoot or on a tile besides your troop" 
    controlsssss1 = " to charge with bayonets."
    Rect(0,0,400, 400, fill='white')
    Label("Help", 200,45,size=40)
    Label(controls, 200,133,size=20)
    Label(controlss, 200,163,size=20)
    Label(controlsss, 200,183,size=20)
    Label(controls1, 200,223,size=20)
    Label(controlss1, 200,253,size=20)
    Label(controlsss1, 200,293,size=20)
    Label(controlssss1, 200, 273,size=20)
    Label(controlsssss1, 200, 313,size=20)

def onMouseMove(mouseX,mouseY):
    if box.contains(mouseX,mouseY):
        box.fill = "Lightgrey"
        box.opacity = 45

    elif plus1.contains(mouseX,mouseY):
        plus1.fill = "Lightgrey"
        plus1.opacity = 45

    elif plus2.contains(mouseX,mouseY):
        plus2.fill = "Lightgrey"
        plus2.opacity = 45

    elif plus3.contains(mouseX,mouseY):
        plus3.fill = "Lightgrey"
        plus3.opacity = 45

    elif back1.contains(mouseX,mouseY):
        back1.fill = "Lightgrey"
        back1.opacity = 45
        
    else:
        box.fill = None
        plus1.fill = None
        plus2.fill = None
        plus3.fill = None
        back1.fill = rgb(72,76,67)
        back1.opacity = 100
        box.opacity = 100
        plus1.opacity = 100
        plus2.opacity = 100
        plus3.opacity = 100

def onMousePress(mouseX, mouseY):
    if plus1.contains(mouseX,mouseY):
        boxes.clear()
    if box.contains(mouseX,mouseY):
        boxes.clear()
        help()
    if plus3.contains(mouseX,mouseY):
        Pic.add(
            Options,
            back1,
            yes
        )
        Options.visible = True
        back1.visible = True
        yes.visible = True
        Pic.toFront()
    if back1.contains(mouseX,mouseY):
        Pic.clear()                
    if plus2.contains(mouseX,mouseY):
        exit()


cmu_graphics.run()