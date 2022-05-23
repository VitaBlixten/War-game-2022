from cmu_graphics import *
from sys import exit

app.playing = False

Options = Image('Installningar.png',0,0,height=400,width=400,visible = False)
back1 = Rect(20,347,85,33,fill=rgb(72,76,67), border='Black',visible = False)
yes = Label('Back',63,363,size=25,fill=rgb(228,224,210),visible = False)

wip = Label("Work in progress", 200,45,size=40,visible = False)
back2 = Rect(20,347,85,33,fill=rgb(72,76,67), border='Black',visible = False)
yes2 = Label('Back',63,363,size=25,fill=rgb(228,224,210),visible = False)

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

multi = Group(

)


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

    elif back2.contains(mouseX,mouseY):
        back2.fill = "Lightgrey"
        back2.opacity = 45
        
    else:
        box.fill = None
        plus1.fill = None
        plus2.fill = None
        plus3.fill = None
        back1.fill = rgb(72,76,67)
        back2.fill = rgb(72,76,67)
        back1.opacity = 100
        back2.opacity = 100
        box.opacity = 100
        plus1.opacity = 100
        plus2.opacity = 100
        plus3.opacity = 100

def onMousePress(mouseX, mouseY):
    if(app.playing == False):
        if plus1.contains(mouseX,mouseY):
            boxes.clear()
            Pic.clear()
            multi.clear()
            app.playing = True 
    if(app.playing == False):
        if box.contains(mouseX,mouseY):
            Pic.clear()
            boxes.clear()
            multi.add(
                back2,
                yes2,
                wip
            )
            wip.visible = True
            back2.visible = True
            yes2.visible = True
            app.playing = True
    if(app.playing == False):
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
            multi.clear()
            boxes.clear()
            app.playing = True
    if back1.contains(mouseX,mouseY):
        Pic.clear()
        boxes.add(
            back,
            box, 
            plus1, 
            plus2,
            plus3, 
        )
        app.playing = False
    if(app.playing == False):                
        if plus2.contains(mouseX,mouseY):
            exit()
    if back2.contains(mouseX,mouseY):
        boxes.add(
            back,
            box, 
            plus1, 
            plus2,
            plus3, 
        )
        multi.clear()    
        app.playing = False

cmu_graphics.run()