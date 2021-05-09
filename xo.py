import turtle
import time

s=turtle.getscreen()
s.title("Tic Tac Toe XO")
wn=turtle.bgcolor("black")
t=turtle.Turtle()
t.hideturtle()
t.penup()

def XOboard():
    t.showturtle()
    t.speed(10)
    t.fillcolor("white")
    t.pensize(10)
    t.goto(150,150)
    t.begin_fill()
    t.pendown()
    for i in range(4):
        t.right(90)
        t.forward(300)
    t.speed(5)
    t.end_fill()
    t.penup()
    t.goto(-150,50)
    t.pendown()
    t.forward(300)
    t.penup()
    t.goto(-150,-50)
    t.pendown()
    t.forward(300)
    t.right(90)
    t.penup()
    t.goto(-50,150)
    t.pendown()
    t.forward(300)
    t.penup()
    t.goto(50,150)
    t.pendown()
    t.forward(300)
    t.penup()
    t.hideturtle()

xxd={1:-150,2:-50,3:50,4:-150,5:-50,6:50,7:-150,8:-50,9:50}
xyd={1:150,2:150,3:150,4:50,5:50,6:50,7:-50,8:-50,9:-50}
oxd={1:-100,2:0,3:100,4:-100,5:0,6:100,7:-100,8:0,9:100}
oyd={1:65,2:65,3:65,4:-35,5:-35,6:-35,7:-135,8:-135,9:-135}

def X(n):
    t.pencolor("black")
    t.penup()
    t.speed(7)
    t.home()
    t.clearstamps()
    t.goto(xxd[n],xyd[n])
    t.forward(15)
    t.right(90)
    t.forward(15)
    t.pendown()
    t.left(45)
    t.forward(70*(2**0.5))
    t.penup()
    t.left(135)
    t.forward(70)
    t.left(135)
    t.pendown()
    t.forward(70*(2**0.5))
    t.penup()
    t.home()
    t.clearstamps()

def O(n):
    t.pencolor("black")
    t.penup()
    t.speed(10)
    t.home()
    t.clearstamps()
    t.goto(oxd[n],oyd[n])
    t.pendown()
    t.circle(35)
    t.penup()
    t.home()
    t.clearstamps()

check=[]
lis1=[1,2,3]
lis2=[4,5,6]
lis3=[7,8,9]

def assign(k):
    global n
    if n in range(1,4):
        lis1[n-1]=k
    elif n in range(4,7):
        lis2[n-4]=k
    elif n in range(7,10):
        lis3[n-7]=k

def chec(lis1,lis2,lis3):
    if lis1[0]==lis2[0]==lis3[0]=="X" or lis1[1]==lis2[1]==lis3[1]=="X" or lis1[2]==lis2[2]==lis3[2]=="X" or lis1[0]==lis1[1]==lis1[2]=="X" or lis2[0]==lis2[1]==lis2[2]=="X" or lis3[0]==lis3[1]==lis3[2]=="X" or lis1[0]==lis2[1]==lis3[2]=="X" or lis1[2]==lis2[1]==lis3[0]=="X":
        if lis1[0]==lis2[0]==lis3[0]:
            t.penup()
            t.pensize(20)
            t.pencolor("red")
            t.goto(-100,125)
            t.pendown()
            t.goto(-100,-125)
            t.penup()
            t.pensize(10)
            t.pencolor("black")
        elif lis1[1]==lis2[1]==lis3[1]:
            t.penup()
            t.pensize(20)
            t.pencolor("red")
            t.goto(0,125)
            t.pendown()
            t.goto(0,-125)
            t.penup()
            t.pensize(10)
            t.pencolor("black")
        elif lis1[2]==lis2[2]==lis3[2]:
            t.penup()
            t.pensize(20)
            t.pencolor("red")
            t.goto(100,125)
            t.pendown()
            t.goto(100,-125)
            t.penup()
            t.pensize(10)
            t.pencolor("black")
        elif lis1[0]==lis1[1]==lis1[2]:
            t.penup()
            t.pensize(20)
            t.pencolor("red")
            t.goto(-125,100)
            t.pendown()
            t.goto(125,100)
            t.penup()
            t.pensize(10)
            t.pencolor("black")
        elif lis2[0]==lis2[1]==lis2[2]:
            t.penup()
            t.pensize(20)
            t.pencolor("red")
            t.goto(-125,0)
            t.pendown()
            t.goto(125,0)
            t.penup()
            t.pensize(10)
            t.pencolor("black")
        elif lis3[0]==lis3[1]==lis3[2]:
            t.penup()
            t.pensize(20)
            t.pencolor("red")
            t.goto(-125,-100)
            t.pendown()
            t.goto(125,-100)
            t.penup()
            t.pensize(10)
            t.pencolor("black")
        elif lis1[0]==lis2[1]==lis3[2]:
            t.penup()
            t.pensize(20)
            t.pencolor("red")
            t.goto(-125,125)
            t.pendown()
            t.goto(125,-125)
            t.penup()
            t.pensize(10)
            t.pencolor("black")
        else:
            t.penup()
            t.pensize(20)
            t.pencolor("red")
            t.goto(125,125)
            t.pendown()
            t.goto(-125,-125)
            t.penup()
            t.pensize(10)
            t.pencolor("black")
        return "X"

    elif lis1[0]==lis2[0]==lis3[0]=="O" or lis1[1]==lis2[1]==lis3[1]=="O" or lis1[2]==lis2[2]==lis3[2]=="O" or lis1[0]==lis1[1]==lis1[2]=="O" or lis2[0]==lis2[1]==lis2[2]=="O" or lis3[0]==lis3[1]==lis3[2]=="O" or lis1[0]==lis2[1]==lis3[2]=="O" or lis1[2]==lis2[1]==lis3[0]=="O":
        
        if lis1[0]==lis2[0]==lis3[0]:
            t.penup()
            t.pensize(20)
            t.pencolor("red")
            t.goto(-100,125)
            t.pendown()
            t.goto(-100,-125)
            t.penup()
            t.pensize(10)
            t.pencolor("black")
        elif lis1[1]==lis2[1]==lis3[1]:
            t.penup()
            t.pensize(20)
            t.pencolor("red")
            t.goto(0,125)
            t.pendown()
            t.goto(0,-125)
            t.penup()
            t.pensize(10)
            t.pencolor("black")
        elif lis1[2]==lis2[2]==lis3[2]:
            t.penup()
            t.pensize(20)
            t.pencolor("red")
            t.goto(100,125)
            t.pendown()
            t.goto(100,-125)
            t.penup()
            t.pensize(10)
            t.pencolor("black")
        elif lis1[0]==lis1[1]==lis1[2]:
            t.penup()
            t.pensize(20)
            t.pencolor("red")
            t.goto(-125,100)
            t.pendown()
            t.goto(125,100)
            t.penup()
            t.pensize(10)
            t.pencolor("black")
        elif lis2[0]==lis2[1]==lis2[2]:
            t.penup()
            t.pensize(20)
            t.pencolor("red")
            t.goto(-125,0)
            t.pendown()
            t.goto(125,0)
            t.penup()
            t.pensize(10)
            t.pencolor("black")
        elif lis3[0]==lis3[1]==lis3[2]:
            t.penup()
            t.pensize(20)
            t.pencolor("red")
            t.goto(-125,-100)
            t.pendown()
            t.goto(125,-100)
            t.penup()
            t.pensize(10)
            t.pencolor("black")
        elif lis1[0]==lis2[1]==lis3[2]:
            t.penup()
            t.pensize(20)
            t.pencolor("red")
            t.goto(-125,125)
            t.pendown()
            t.goto(125,-125)
            t.penup()
            t.pensize(10)
            t.pencolor("black")
        else:
            t.penup()
            t.pensize(20)
            t.pencolor("red")
            t.goto(125,125)
            t.pendown()
            t.goto(-125,-125)
            t.penup()
            t.pensize(10)
            t.pencolor("black")
            
        return "O"
    elif turn==9:
        return "nil"

def execution(x,y):
    global turn
    k=turn%2
    global n
    n=0
    
    if turn<10:
        
        if y<150 and y>50:
            
            if x>-150 and x<-50:
                n=1
            elif x>-50 and x<50:
                n=2
            elif x>50 and x<150:
                n=3
                
        elif y<50 and y>-50:
            
            if x>-150 and x<-50:
                n=4
            elif x>-50 and x<50:
                n=5
            elif x>50 and x<150:
                n=6
                
        elif y<-50 and y>-150:
            
            if x>-150 and x<-50:
                n=7
            elif x>-50 and x<50:
                n=8
            elif x>50 and x<150:
                n=9
            
        if n not in check and n!=0:
            
            check.append(n)
            
            if k!=0:
                X(n)
                assign("X")
            else:
                O(n)
                assign("O")
                
            c=chec(lis1,lis2,lis3)
            
            if c=="X":
                time.sleep(1)
                t.clear()
                t.penup()
                t.home()
                t.clearstamps()
                t.pendown()
                t.pencolor("white")
                t.write("X Won")
            elif c=="O":
                time.sleep(1)
                t.clear()
                t.penup()
                t.home()
                t.clearstamps()
                t.pendown()
                t.pencolor("white")
                t.write("O Won")
            elif c=="nil":
                time.sleep(1)
                t.clear()
                t.penup()
                t.home()
                t.clearstamps()
                t.pendown()
                t.pencolor("white")
                t.write("Game Drawn")
            
            turn+=1

t.pencolor("white")
t.write("Game of XO \nDo Not Click Until One Turn Is Over")
time.sleep(4)
t.clear()
t.pencolor("black")
XOboard()
s.listen(0,0)
turn=1
s.onclick(execution)
s.mainloop()
