
import simplegui
import random

# load card sprite
CARD_SIZE = (73,98)
CARD_CENTER = (36.5,49)
CARD_IMAGE = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71,96)
CARD_BACK = simplegui.load_image("")

# init global variables
deck = []
in_play = False
outcome = ""
score = 0

# define card globals
SUITS = ('C','S','H','D')
RANKS = ('A','2','3','4','5','6','7','8','9','T','J','Q','K')
VALUES = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':10,'Q':10,'K':10}

# define card class
class Card:
    def __init__(self,suit,rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit=suit
            self.rank=rank
        else:
            self.suit=None
            self.rank=None
            print("Invalid Card: "+suit+rank)

    def __str__(self):
        return self.suit+self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def get_value(self):
        return VALUES[self.rank]

    def draw(self,canvas,pos):
        card_pos = (CARD_CENTER[0]+CARD_SIZE[0]*RANKS.index(self.rank),
                    CARD_CENTER[1]+CARD_SIZE[1]*SUITS.index(self.suit))
        canvas.draw_image(CARD_IMAGE,card_pos,CARD_SIZE,[pos[0]+CARD_CENTER[0],pos[1]+CARD_CENTER[1]],CARD_SIZE)


class Hand:
    def __init__(self):
        self.cards=[]
        pass

    def __str__(self):
        for card in self.cards:
            print(card+'\t')

    def add_card(self,card):
        self.cards.append(card)

    def get_value(self):
        hand_value=0
        hasAces=False
        for card in self.cards:
            hand_value+=card.get_value()
            if card.rank=='A':
                hasAces=True
        if not hasAces:
            return hand_value
        else:
            if hand_value+10<=21:
                return hand_value+10
            else:
                return hand_value

    def busted(self):
        if self.get_value()>21:
            return True
        else:
            return False

    def clear(self):
        self.cards=[]

class Deck:
    def __init__(self):
        self.allCards=[]
        for s in SUITS:
            for r in RANKS:
                self.allCards.append(Card(s,r))

    def shuffle(self):
        random.shuffle(self.allCards)

    def deal_cards(self):
        pass

def deal():
    global outcome,in_play,player,computer,outcome,deck

    outcome=""
    player.clear()
    computer.clear()

    # deck=Deck()
    tempCard=deck.allCards.pop()
    player.add_card(tempCard)
    tempCard=deck.allCards.pop()
    computer.add_card(tempCard)

    tempCard=deck.allCards.pop()
    player.add_card(tempCard)
    tempCard=deck.allCards.pop()
    computer.add_card(tempCard)

    in_play=True

def hit():
    global in_play,score,player,computer,outcome
    if in_play:
        newCard=deck.allCards.pop()
        player.add_card(newCard)

    if player.busted():
        print("You Lose")
        score-=1
        outcome="You Lose"
        in_play=False
    else:
        who_win()

def stand():
    global computer,player,deck,score,in_play
    while computer.get_value()<17:
        tempCard=deck.allCards.pop()
        computer.add_card(tempCard)
    who_win()


def who_win():
    global score,player,computer,outcome
    if player.get_value()>computer.get_value():
        print("You Win")
        outcome="You Win"
        score+=1
    elif player.get_value()==computer.get_value():
        print("Card Value Tie, You Lose")
        outcome="Card Value Tie, You Lose"
        score-=1
    elif player.get_value()<computer.get_value():
        print("You Lose")
        outcome="You Lose"
        score-=1

def draw(canvas):
    pos=[100,200]
    for card in computer.cards:
        card.draw(canvas,pos)
        pos[0]+=CARD_BACK_SIZE[0]

    pos[0]=100
    pos[1]=pos[1]+CARD_BACK_SIZE[1]+120
    for card in player.cards:
        card.draw(canvas,pos)
        pos[0]+=CARD_BACK_SIZE[0]

    canvas.draw_text("Blackjack",[80,100],60,"Black")
    canvas.draw_text("Dealer",[50,180],40,"White")
    canvas.draw_text("You",[50,400],40,"White")
    canvas.draw_text(outcome,[400,140],40,"Red")

player=Hand()
computer=Hand()
deck=Deck()

frame=simplegui.create_frame("Blackjack",600,600)
frame.set_canvas_background("Green")
frame.set_draw_handler(draw)
frame.add_button("Deal",deal,100)
frame.add_button("Hit",hit,100)
frame.add_button("Stand",stand,100)

frame.start()
deal()
