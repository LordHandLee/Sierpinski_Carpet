import turtle as t

t.setup(900,900)
c = t.Turtle()
t.speed('fastest')
t.bgcolor('black')
t.delay(0)
colorlist = ["blue", "purple", "green"]
x = 0
y = 0
dim1 = 300

def drawFilledRectangle(n,t, x, y, w, h, colorP="black", colorF="black"):
    t.pencolor(colorP)
    t.fillcolor(colorF)
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    t.goto(x+w, y)
    t.goto(x+w, y+h)
    t.goto(x, y+h)
    t.goto(x, y)
    t.end_fill()
    
def func(dim,n,x,y):
        colorF = colorlist[n%3]
        if n == 1:
            drawFilledRectangle(n,t,x+dim/3, y+dim/3, dim/3, dim/3, colorF, colorF)
            return 1
        elif n > 1:
            drawFilledRectangle(n,t,x+dim/3, y+dim/3, dim/3, dim/3, colorF, colorF)
            func(dim/3,n-1,x+dim/3,y)
            func(dim/3,n-1,x,y+dim/3)
            func(dim/3,n-1,x+2*dim/3,y)
            func(dim/3,n-1,x,y+2*dim/3)
            func(dim/3,n-1,x,y)
            func(dim/3,n-1,x+2*dim/3,y+2*dim/3)
            func(dim/3,n-1,x+dim/3,y+2*dim/3)
            func(dim/3,n-1,x+2*dim/3,y+dim/3)

        


func(900,5,-450,-450)
