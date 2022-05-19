from cmu_graphics import *

####Picketts charge at gettysburg###
###Map
###to do: add frendly fire


Rect(0, 0, 400, 400, fill="forestgreen")
app.steps = 0
app.turn = True
app.col = 6
app.row = 6
app.hej = makeList(app.col,app.row)
app.selectedRow = -1
app.selectedCol = -1
import Trees

def findsold(x, y):
    # Find which block was clicked.
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
        hej = Rect(x,y,400/7,400/7,fill=None,border='black')
        app.hej[row][col] = hej


###Interface


###soldiers
for row in range(app.row):
    x = row*60 + 25.2 
    redsold = Rect(x, 45, 50, 15, fill="DarkBlue", border='black', borderWidth=1)
    bluesold = Rect(x, 345, 50, 15, fill="Red", border='black', borderWidth=1)
    app.grid[row][0] = redsold
    app.grid[row][5] = bluesold


###firing




###Vibility

###find soldider
###Movement
def swap(row1, col1, row2, col2):
    # Swaps the fills of the blocks at (row1, col1) and (row2, col2).
    X1 = app.grid[row1][col1].centerX
    Y1 = app.grid[row1][col1].centerY
    X2 = app.grid[row2][col2].centerX
    Y2 = app.grid[row2][col2].centerY
    app.grid[row1][col1].centerX = X2
    app.grid[row1][col1].centerY = Y2
    app.grid[row2][col2].centerX = X1
    app.grid[row2][col2].centerY = Y1
def onMousePress(MouseX, MouseY):



cmu_graphics.run()