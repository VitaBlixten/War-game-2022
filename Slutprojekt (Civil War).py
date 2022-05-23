from cmu_graphics import *
import math
####Picketts charge at gettysburg###
###Map
###to do: add frendly fire

Rect(0, 0, 400, 400, fill="forestgreen")
app.steps = 0
app.turn = True
app.col = 6
app.row = 6
app.grid = makeList(app.col,app.row)
app.selectedRow = -1
app.selectedCol = -1
app.phase = "movement"
import Trees

def findsold(x, y):
    for row in range(app.row):
        for col in range(app.col):
            sold = app.grid[row][col]
            if sold.hits(x, y):
                app.selectedRow = row
                app.selectedCol = col
                return sold



###2D list
for row in range(app.row):
    for col in range(app.col):
        x = row*60 + 22
        y =col*60 +22 
        Rect(x,y,400/7,400/7,fill="green", border="black")
        if col == 0:
            redsold = Group(Rect(x,y,400/7,400/7,fill="green", border="black") , Rect(x+3.2 , 45, 50, 15, fill="DarkBlue", border='black', borderWidth=1))
            app.grid[row][0] = redsold
        elif col == 5:
            bluesold = Group(Rect(x,y,400/7,400/7,fill="green", border="black") , Rect(x+3.2 , 45, 50, 15, fill="Red", border='black', borderWidth=1))
            app.grid[row][5] = bluesold
        
        else:
            hej = Rect(x,y,400/7,400/7,fill="yellow", opacity=50)
            app.grid[row][col] = hej
            
        


###Interface


###soldiers
'''
for row in range(app.row):
    x = row*60 + 25.2 
    redsold = Rect(x, 45, 50, 15, fill="DarkBlue", border='black', borderWidth=1)
    bluesold = Grupp(Rect(x, 345, 50, 15, fill="Red", border='black', borderWidth=1))
    app.grid[row][0] = redsold
    app.grid[row][5] = bluesold
'''

###firing
def shooting(col1, col2, row1, row2):
    ### Kolla att kraven för att avfyra ett skott uppfylls
   
    ### Hitta avståndet mellan skytten och målet
    distance = abs(col1 - col2)
    ### Kolla om det träffar baserat på avståndet
    
    
    ### Beräkna skadan om den träffar
    if distance > 4:
        damage = 0
    elif distance > 2:
        damage = randrange(0,5)
    elif distance > 0:
        damage = randrange(2,10) 


    app.grid[row2][col2].value -= damage
    pass



###Vibility

###find soldider
###Movement
def swap(row1, col1, row2, col2):
    # Swaps the fills of the blocks at (row1, col1) and (row2, col2).
    X2 = app.grid[row2][col2].centerX
    Y2 = app.grid[row2][col2].centerY
    app.grid[row1][col1].centerX = X2
    app.grid[row1][col1].centerY = Y2
    app.grid[row1][col1] = app.grid[row2][col2]
    app.grid[row2][col2] = hej

         

def onMousePress(mouseX, mouseY):
    if app.phase == "movement":
        row1 = -1
        col1 = -1

        # If a block was already clicked, stores its values.
        if (app.selectedRow != -1):
            row1 = app.selectedRow
            col1 = app.selectedCol
        block = findsold(mouseX, mouseY)

        # Second time a block was clicked.
        if ((block != None) and (row1 != -1)):
            # Swaps the colors.
            if app.grid[app.selectedRow][app.selectedCol] == hej:
                swap(row1, col1, app.selectedRow, app.selectedCol)

                # Resets the selected row and col and update the correct blocks.
                app.selectedRow = -1
                app.selectedCol = -1

def onKeyPress(key):
    if key == 'm':
        app.phase = "movement"
        pass

    if key == 'k':
        pass
    pass

cmu_graphics.run()