from cmu_graphics import *

###Box
back = Rect(0,0,400, 400, fill='white')
box = Rect(120,200,160,50,fill=None, border='Black')
plus1 = Rect(120,110,160,50,fill=None, border='Black')
plus2 = Rect(120,290,160,50,fill=None, border='Black')

boxes = Group(
back,
box, 
plus1, 
plus2, 
Label("War", 200,45,size=40),
Label("Play", 200,133,size=30),
Label("Help", 200,223,size=30),
Label("Something", 200,313,size=30))

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
    elif plus1.contains(mouseX,mouseY):
        plus1.fill = "Lightgrey"
    
    elif plus2.contains(mouseX,mouseY):
        plus2.fill = "Lightgrey"
        
    else:
        box.fill = None
        plus1.fill = None
        plus2.fill = None

def onMousePress(mouseX, mouseY):
    if plus1.contains(mouseX,mouseY):
        boxes.clear()
    if box.contains(mouseX,mouseY):
        boxes.clear()
        help()

cmu_graphics.run()