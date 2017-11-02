from graphics import *
from random import *

win=GraphWin('mouse click', 1000, 500)
win.setBackground("#0a3b5e")
block=[]
xcor1=[]
ycor1=[]
xcor2=[]
ycor2=[]
mineblock=[]
doneblock=[]
box=0
totalscore=0
score=[1,2,3,4,5,6,7,8,9,32,33,34,35,36,37,38,39,10,31,56,57,58,59,60,61,40,11,30,55,72,73,74,75,62,41,12,29,54,71,80,81,76,63,42,13,28,53,70,79,78,77,64,43,14,27,52,69,68,67,66,65,44,15,26,51,50,49,48,47,46,45,16,25,24,23,22,21,20,19,18,17]
mouseclick=0
##------------
def board():
    global boxcenter
    i=0
    colorindic=0
    while (i!=450):
        i=i+50
        j=0
        while (j!=450):
            j=j+50
            p1=Point(i,j)
            x1=p1.getX()
            y1=p1.getY()
            xcor1.append(x1)
            ycor1.append(y1)
            p2=Point(i+50,j+50)
            x2=p2.getX()
            y2=p2.getY()
            xcor2.append(x2)
            ycor2.append(y2)
            if (colorindic==0):
                colorindic=1
                r1=Rectangle(p1,p2)
                r1.setFill("red")
                r1.draw(win)
                block.append(r1)
                continue
            if (colorindic==1):
                colorindic=0
                r2=Rectangle(p1,p2)
                r2.setFill("blue")
                r2.draw(win)
                block.append(r2)
    scoretitle=Text(Point(600,200),"SCORE : ")
    scoretitle.setFace("helvetica")
    scoretitle.setStyle("bold italic")
    scoretitle.setTextColor("Red")
    scoretitle.setSize(20)
    scoretitle.draw(win)
    moveshow=Text(Point(600,100),"MOVES LEFT : ")
    moveshow.setFace("helvetica")
    moveshow.setStyle("bold italic")
    moveshow.setTextColor("Red")
    moveshow.setSize(13)
    moveshow.draw(win)
    minecount=0
    while(minecount!=36):
        mine=randint(0,80)
        mineblock.append(mine)
        minecount=minecount+1
##------------
def mymove():
    global boxcenter
    global block
    global box
    global totalscore
    global doneblock
    movesleft=30
    moveleftshow=Text(Point(700,100), movesleft)
    moveleftshow.setFace("helvetica")
    moveleftshow.setStyle("bold italic")
    moveleftshow.setTextColor("Red")
    moveleftshow.setSize(20)
    moveleftshow.draw(win)
    gameend=0
    while(gameend!=30):
        coverp1=Point(660,175)
        coverp2=Point(800,225)
        cover=Rectangle(coverp1, coverp2)
        cover.setFill("#0a3b5e")
        cover.draw(win)
        finalscore=Text(Point(700,200), totalscore)
        finalscore.setFace("helvetica")
        finalscore.setStyle("bold italic")
        finalscore.setTextColor("Red")
        finalscore.setSize(20)
        finalscore.draw(win)
        mouseclick=win.getMouse()
        x=mouseclick.getX()
        y=mouseclick.getY()
        if (x<50):
            continue
        if (x>500):
            continue
        if (y<50):
            continue
        if (y>500):
            continue
        movesleft=movesleft-1
        movecoverp1=Point(660,75)
        movecoverp2=Point(800,125)
        movecover=Rectangle(movecoverp1, movecoverp2)
        movecover.setFill("#0a3b5e")
        movecover.draw(win)
        moveleftshow=Text(Point(700,100), movesleft)
        moveleftshow.setFace("helvetica")
        moveleftshow.setStyle("bold italic")
        moveleftshow.setTextColor("Red")
        moveleftshow.setSize(20)
        moveleftshow.draw(win)
        checkblock=-1
        while (checkblock!=80):
            checkblock=checkblock+1
            if(x>xcor1[checkblock]):
                if(x<xcor2[checkblock]):
                    if(y>ycor1[checkblock]):
                        if(y<ycor2[checkblock]):
                            box=checkblock
                            break
                        continue
                    continue
                continue
            continue
        if (box in doneblock):
            gameend=gameend+1
            continue
        doneblock.append(box)
        if (box in mineblock):
            block[box].undraw()
            block[box].setFill("black")
            block[box].draw(win)
            totalscore=totalscore-score[box]
            gameend=gameend+1
            continue
        if (score[box]<57):
            block[box].undraw()
            block[box].setFill("green")
            block[box].draw(win)
        if (score[box]>56):
            if (score[box]<73):
                block[box].undraw()
                block[box].setFill("purple")
                block[box].draw(win)
        if (score[box]>72):
            block[box].undraw()
            block[box].setFill("yellow")
            block[box].draw(win)
        totalscore=totalscore+score[box]
        gameend=gameend+1
    gameover=Text(Point(600,250),"GAME OVER")
    gameover.setFace("helvetica")
    gameover.setStyle("bold italic")
    gameover.setTextColor("#5e0a11")
    gameover.setSize(20)
    gameover.draw(win)
##----------------   
board()
mymove()

