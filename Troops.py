from cmu_graphics import *

###Confederat soldiers
conSoldier1 = Rect(25, 350, 50, 15, fill="darkGray", border='black', borderWidth=1)
PlayerIcon1 = Polygon(25+25, 345, 25+25-10, 345-10, 25+25+10, 345-10, fill='gold', border='black', borderWidth=1, visible=False)
con1 = Group(conSoldier1, PlayerIcon1)
conSoldier2 = Rect(100, 350, 50, 15, fill="darkGray", border='black', borderWidth=1)
PlayerIcon2 = Polygon(100+25, 345, 100+25-10, 345-10, 100+25+10, 345-10, fill='gold', border='black', borderWidth=1, visible=False)
con2 = Group(conSoldier2, PlayerIcon2)
conSoldier3 = Rect(175, 350, 50, 15, fill="darkGray", border='black', borderWidth=1)
PlayerIcon3 = Polygon(175+25, 345, 175+25-10, 345-10, 175+25+10, 345-10, fill='gold', border='black', borderWidth=1, visible=False)
con3 = Group(conSoldier3, PlayerIcon3)
conSoldier4 = Rect(250, 350, 50, 15, fill="darkGray", border='black', borderWidth=1)
PlayerIcon4 = Polygon(250+25, 345, 250+25-10, 345-10, 250+25+10, 345-10, fill='gold', border='black', borderWidth=1, visible=False)
con4 = Group(conSoldier4, PlayerIcon4)
conSoldier5 = Rect(325, 350, 50, 15, fill="darkGray", border='black', borderWidth=1)
PlayerIcon5 = Polygon(325+25, 345, 325+25-10, 345-10, 325+25+10, 345-10, fill='gold', border='black', borderWidth=1, visible=False)
con5 = Group(conSoldier5, PlayerIcon5)

###Union soldiers
unSoldier1 = Rect(25, 50, 50, 15, fill="DarkBlue", border='black', borderWidth=1)
Player2Icon1 = Polygon(25+25, 40, 25+25-10, 40-10, 25+25+10, 40-10, fill='crimson', border='black', borderWidth=1, visible=False)
un1 = Group(unSoldier1, Player2Icon1)
unSoldier2 = Rect(100, 50, 50, 15, fill="DarkBlue", border='black', borderWidth=1)
Player2Icon2 = Polygon(100+25, 40, 100+25-10, 40-10, 100+25+10, 40-10, fill='crimson', border='black', borderWidth=1, visible=False)
un2 = Group(unSoldier2, Player2Icon2)
unSoldier3 = Rect(175, 50, 50, 15, fill="DarkBlue", border='black', borderWidth=1)
Player2Icon3 = Polygon(175+25, 40, 175+25-10, 40-10, 175+25+10, 40-10, fill='crimson', border='black', borderWidth=1, visible=False)
un3 = Group(unSoldier3, Player2Icon3)
unSoldier4 = Rect(250, 50, 50, 15, fill="DarkBlue", border='black', borderWidth=1)
Player2Icon4 = Polygon(250+25, 40, 250+25-10, 40-10, 250+25+10, 40-10, fill='crimson', border='black', borderWidth=1, visible=False)
un4 = Group(unSoldier4, Player2Icon4)
unSoldier5 = Rect(325, 50, 50, 15, fill="DarkBlue", border='black', borderWidth=1)
Player2Icon5 = Polygon(325+25, 40, 325+25-10, 40-10, 325+25+10, 40-10, fill='crimson', border='black', borderWidth=1, visible=False)
un5 = Group(unSoldier5, Player2Icon5)

###firing
confire1 = Arc(3000, conSoldier1.centerY-5, 200, 100, conSoldier1.rotateAngle - 22, 45, fill=gradient("white", "silver", "darkgray", start="top"), visible=False)
confire2 = Arc(3000, conSoldier2.centerY-5, 200, 100, conSoldier2.rotateAngle - 22, 45, fill=gradient("white", "silver", "darkgray", start="top"), visible=False)
confire3 = Arc(3000, conSoldier3.centerY-5, 200, 100, conSoldier3.rotateAngle - 22, 45, fill=gradient("white", "silver", "darkgray", start="top"), visible=False)
confire4 = Arc(3000, conSoldier4.centerY-5, 200, 100, conSoldier4.rotateAngle - 22, 45, fill=gradient("white", "silver", "darkgray", start="top"), visible=False)
confire5 = Arc(3000, conSoldier5.centerY-5, 200, 100, conSoldier5.rotateAngle - 22, 45, fill=gradient("white", "silver", "darkgray", start="top"), visible=False)
con1.add(confire1)
con2.add(confire2)
con3.add(confire3)
con4.add(confire4)
con5.add(confire5)

unfire1 = Arc(3000, unSoldier1.centerY-5, 200, 100, unSoldier1.rotateAngle - 22-180, 45, fill=gradient("white", "silver", "darkgray", start="top"), visible=False)
unfire2 = Arc(3000, unSoldier2.centerY-5, 200, 100, unSoldier2.rotateAngle - 22-180, 45, fill=gradient("white", "silver", "darkgray", start="top"), visible=False)
unfire3 = Arc(3000, unSoldier3.centerY-5, 200, 100, unSoldier3.rotateAngle - 22-180, 45, fill=gradient("white", "silver", "darkgray", start="top"), visible=False)
unfire4 = Arc(3000, unSoldier4.centerY-5, 200, 100, unSoldier4.rotateAngle - 22-180, 45, fill=gradient("white", "silver", "darkgray", start="top"), visible=False)
unfire5 = Arc(3000, unSoldier5.centerY-5, 200, 100, unSoldier5.rotateAngle - 22-180, 45, fill=gradient("white", "silver", "darkgray", start="top"), visible=False)
un1.add(unfire1)
un2.add(unfire2)
un3.add(unfire3)
un4.add(unfire4)
un5.add(unfire5)

###Vibility
PlayerIcon1.visible = False
PlayerIcon2.visible = False
PlayerIcon3.visible = False
PlayerIcon4.visible = False
PlayerIcon5.visible = False

confire1.visible = False
confire2.visible = False
confire3.visible = False
confire4.visible = False
confire5.visible = False

Player2Icon1.visible = False
Player2Icon2.visible = False
Player2Icon3.visible = False
Player2Icon4.visible = False
Player2Icon5.visible = False

unfire1.visible = False
unfire2.visible = False
unfire3.visible = False
unfire4.visible = False
unfire5.visible = False

def onKeyPress(key):
if(confire1.hitsShape(unSoldier1) == True):
        un1.visible = False
    if(confire2.hitsShape(unSoldier2) == True):
        un2.visible = False
    if(confire3.hitsShape(unSoldier3) == True):
        un3.visible = False
    if(confire4.hitsShape(unSoldier4) == True):
        un4.visible = False
    if(confire5.hitsShape(unSoldier5) == True):
        un5.visible = False

    if(unfire1.hitsShape(conSoldier1) == True):
        con1.visible = False
    if(unfire2.hitsShape(conSoldier2) == True):
        con2.visible = False
    if(unfire3.hitsShape(conSoldier3) == True):
        con3.visible = False
    if(unfire4.hitsShape(conSoldier4) == True):
        con4.visible = False
    if(unfire5.hitsShape(conSoldier5) == True):
        con5.visible = False
        
###Player1
    if(PlayerIcon1.visible == True):
        if(key == "up"): 
            con1.centerY -= 10
        elif(key == "down"):
            con1.centerY += 10
        elif(key == "left"):
            conSoldier1.rotateAngle -= 10
            confire1.rotateAngle -= 10
        elif(key == "right"):
            conSoldier1.rotateAngle += 10
            confire1.rotateAngle += 10
        elif(key == "-"):
            confire1.visible = True
            confire1.centerX = conSoldier1.centerX
            confire1.centerY = conSoldier1.centerY-5

    if(PlayerIcon2.visible == True):
        if(key == "up"): 
            con2.centerY -= 10
        elif(key == "down"):
            con2.centerY += 10
        elif(key == "left"):
            conSoldier2.rotateAngle -= 10
            confire2.rotateAngle -= 10
        elif(key == "right"):
            conSoldier2.rotateAngle += 10
            confire2.rotateAngle += 10
        elif(key == "-"):
            confire2.visible = True
            confire2.centerX = conSoldier2.centerX
            confire2.centerY = conSoldier2.centerY-5

    
        
    if(PlayerIcon3.visible == True):
        if(key == "up"): 
            con3.centerY -= 10
        elif(key == "down"):
            con3.centerY += 10
        elif(key == "left"):
            conSoldier3.rotateAngle -= 10
            confire3.rotateAngle -= 10
        elif(key == "right"):
            conSoldier3.rotateAngle += 10
            confire3.rotateAngle += 10
        elif(key == "-"):
            confire3.visible = True
            confire3.centerX = conSoldier3.centerX
            confire3.centerY = conSoldier3.centerY-5
    
    if(PlayerIcon4.visible == True):
        if(key == "up"): 
            con4.centerY -= 10
        elif(key == "down"):
            con4.centerY += 10
        elif(key == "left"):
            conSoldier4.rotateAngle -= 10
            confire4.rotateAngle -= 10
        elif(key == "right"):
            conSoldier4.rotateAngle += 10
            confire4.rotateAngle += 10
        elif(key == "-"):
            confire4.visible = True
            confire4.centerX = conSoldier4.centerX
            confire4.centerY = conSoldier4.centerY-5
            
    if(PlayerIcon5.visible == True):
        if(key == "up"): 
            con5.centerY -= 10
        elif(key == "down"):

            con5.centerY += 10
        elif(key == "left"):
            conSoldier5.rotateAngle -= 10
            confire5.rotateAngle -= 10
        elif(key == "right"):
            conSoldier5.rotateAngle += 10
            confire5.rotateAngle += 10
        elif(key == "-"):
            confire5.visible = True
            confire5.centerX = conSoldier5.centerX
            confire5.centerY = conSoldier5.centerY-5


    if(key == "7"):
        if (PlayerIcon1.visible == False and app.turn == False):
            PlayerIcon1.visible = True
        else:
            PlayerIcon1.visible = False
    if(key == "8"):
        if (PlayerIcon2.visible == False and app.turn == False):
            PlayerIcon2.visible = True
        else:
            PlayerIcon2.visible = False
    if(key == "9"):
        if (PlayerIcon3.visible == False and app.turn == False):
            PlayerIcon3.visible = True
        else:
            PlayerIcon3.visible = False        
    if(key == "0"):
        if (PlayerIcon4.visible == False and app.turn == False):
            PlayerIcon4.visible = True
        else:
            PlayerIcon4.visible = False
    if(key == "+"):
        if (PlayerIcon5.visible == False and app.turn == False):
            PlayerIcon5.visible = True
        else:
            PlayerIcon5.visible = False

###Player2    
    if(Player2Icon1.visible == True):
        if(key == "s"): 
            un1.centerY -= 10
        elif(key == "w"):
            un1.centerY += 10
        elif(key == "d"):
            unSoldier1.rotateAngle -= 10
            unfire1.rotateAngle -= 10
        elif(key == "a"):
            unSoldier1.rotateAngle += 10
            unfire1.rotateAngle += 10
        elif(key == "f"):
            unfire1.visible = True
            unfire1.centerX = unSoldier1.centerX
            unfire1.centerY = unSoldier1.centerY+5
    
    
    
    if(Player2Icon2.visible == True):
        if(key == "s"): 
            un2.centerY -= 10
        elif(key == "w"):
            un2.centerY += 10
        elif(key == "d"):
            unSoldier2.rotateAngle -= 10
            unfire2.rotateAngle -= 10
        elif(key == "a"):
            unSoldier2.rotateAngle += 10
            unfire2.rotateAngle += 10
        elif(key == "f"):
            unfire2.visible = True
            unfire2.centerX = unSoldier2.centerX
            unfire2.centerY = unSoldier2.centerY+5
    
        
    if(Player2Icon3.visible == True):
        if(key == "s"): 
            un3.centerY -= 10
        elif(key == "w"):
            un3.centerY += 10
        elif(key == "d"):
            unSoldier3.rotateAngle -= 10
            unfire3.rotateAngle -= 10
        elif(key == "a"):
            unSoldier3.rotateAngle += 10
            unfire3.rotateAngle += 10
        elif(key == "f"):
            unfire3.visible = True
            unfire3.centerX = unSoldier3.centerX
            unfire3.centerY = unSoldier3.centerY+5
    
    if(Player2Icon4.visible == True):
        if(key == "s"): 
            un4.centerY -= 10
        elif(key == "w"):
            un4.centerY += 10
        elif(key == "d"):
            unSoldier4.rotateAngle -= 10
            unfire4.rotateAngle -= 10
        elif(key == "a"):
            unSoldier4.rotateAngle += 10
            unfire4.rotateAngle += 10
        elif(key == "f"):
            unfire4.visible = True
            unfire4.centerX = unSoldier4.centerX
            unfire4.centerY = unSoldier4.centerY+5
            
    if(Player2Icon5.visible == True):
        if(key == "s"): 
            un5.centerY -= 10
        elif(key == "w"):
            un5.centerY += 10
        elif(key == "d"):
            unSoldier5.rotateAngle -= 10
            unfire5.rotateAngle -= 10
        elif(key == "a"):
            unSoldier5.rotateAngle += 10
            unfire5.rotateAngle += 10
        elif(key == "f"):
            unfire5.visible = True
            unfire5.centerX = unSoldier5.centerX
            unfire5.centerY = unSoldier5.centerY+5

    
    if(key == "1"):
        if (Player2Icon1.visible == False and app.turn == True):
            Player2Icon1.visible = True
        else:
            Player2Icon1.visible = False
    if(key == "2"):
        if (Player2Icon2.visible == False and app.turn == True):
            Player2Icon2.visible = True
        else:
            Player2Icon2.visible = False
    if(key == "3"):
        if (Player2Icon3.visible == False and app.turn == True):
            Player2Icon3.visible = True
        else:
            Player2Icon3.visible = False        
    if(key == "4"):
        if (Player2Icon4.visible == False and app.turn == True):
            Player2Icon4.visible = True
        else:
            Player2Icon4.visible = False
    if(key == "5"):
        if (Player2Icon5.visible == False and app.turn == True):
            Player2Icon5.visible = True
        else:
            Player2Icon5.visible = False
            
    
    
    ###Fire
    confire1.toBack()
    confire2.toBack()
    confire3.toBack()
    confire4.toBack() 
    confire5.toBack()

    unfire1.toBack()
    unfire2.toBack()
    unfire3.toBack() 
    unfire4.toBack()
    unfire5.toBack()

def onStep():    
        app.steps += 1
        if(app.steps >= 150):
            if app.turn == True:
                Player2Icon1.visible = False
                Player2Icon2.visible = False
                Player2Icon3.visible = False
                Player2Icon4.visible = False
                Player2Icon5.visible = False
                unfire1.centerX = 3000
                unfire2.centerX = 3000
                unfire3.centerX = 3000
                unfire4.centerX = 3000
                unfire5.centerX = 3000
                Round.value = "Confederate turn"
                app.turn = False
                
            else:
                PlayerIcon1.visible = False
                PlayerIcon2.visible = False
                PlayerIcon3.visible = False
                PlayerIcon4.visible = False
                PlayerIcon5.visible = False
                confire1.centerX = 3000
                confire2.centerX = 3000
                confire3.centerX = 3000
                confire4.centerX = 3000
                confire5.centerX = 3000
                Round.value = "Union turn"
                app.turn = True 
            app.steps = 0