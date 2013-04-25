
import simplegui
import random

numbers=[]
cards=[]
firstTry=[-1,0]
secondTry=[-2,0]
state=0
move=0

def init():
    global numbers,cards
    global firstTry, secondTry
    global state
    numbers = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
    random.shuffle(numbers)
    cards=[]
    for number in numbers:
        cards.append([number,0])
    firstTry=-1
    secondTry=-1
    state=0

def mouseClick(pos):
    global firstTry, secondTry, cards, state, move
    move=move+1
    if state==0:
        index=pos[0]//50
        firstTry=cards[index]
        firstTry[1]=1
        cards[index]=firstTry
        state=1
    elif state==1:
        index=pos[0]//50
        secondTry=cards[index]
        secondTry[1]=1
        cards[index]=secondTry
        state=2
    elif state==2:
        if firstTry in cards and secondTry in cards:
            if firstTry[0]!=secondTry[0]:
                cards[cards.index(firstTry)]=[firstTry[0],0]
                cards[cards.index(secondTry)]=[secondTry[0],0]
        index=pos[0]//50
        firstTry=cards[index]
        firstTry[1]=1
        cards[index]=firstTry
        state=1
        secondTry=[]


def draw(canvas):
    global cards,move,moveLabel
    p=[0,100]
    moveLabel.set_text("Move = "+str(move))
    for card in cards:
        if card[1]==1:
            canvas.draw_text(str(card[0]),p,90,"White")
        p[0]=p[0]+50


frame=simplegui.create_frame("Memory",800,100)
frame.add_button("Restart",init)
moveLabel=frame.add_label("Move = 0")

init()

frame.set_mouseclick_handler(mouseClick)
frame.set_draw_handler(draw)

frame.start()