#Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# global variables for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

win = 0
lost = 0
#card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
#hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.card_lst = []

    def __str__(self):
        # return a string representation of a hand
        printstr = "Hand contains: "
        for i in self.card_lst:
            printstr += i.get_suit() + i.get_rank() + " "
         
        return printstr

    def add_card(self, card):
        # add a card object to a hand
        self.card_lst.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand
        val = 0
        count = 0
        for i in self.card_lst:
            val += VALUES[i.rank]
            if i.rank == 'A':
                count += 1
        
            
        #if count == 1:
        #    val += 10
        #elif (count == 2) and (len(self.card_lst) < 3):
        #    val += 10
            
        for i in range(0,count):
            if val+10 <= 21:
                val += 10
        
        return val
                    
   
    def draw(self, canvas, pos):
        # draw a hand
        j = 0
        for i in self.card_lst:
            tmppos = [pos[0] + (CARD_SIZE[0]+5)*j, pos[1]]
            i.draw(canvas, tmppos)
            j += 1

        
#deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck_lst = []
        for i in SUITS:
            for j in RANKS:
                self.deck_lst.append(Card(i,j))
                        

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck_lst)
        

    def deal_card(self):
        # deal a card object from the deck
        return self.deck_lst.pop()
        
    
    def __str__(self):
        # return a string representing the deck
        printstr = "Deck contains"
        for i in self.deck_lst:
            printstr += i.get_suit() + i.get_rank() + " "
        
        return printstr
            

# event handlers for buttons
def deal():
    global outcome, in_play, deck, playerhand, dealerhand, lost, win
    if in_play:
        lost += 1
        
    outcome = ""
    deck = Deck()
    deck.shuffle()
    
    playerhand = Hand()
    dealerhand = Hand()
    
    playerhand.add_card(deck.deal_card())
    playerhand.add_card(deck.deal_card())

    dealerhand.add_card(deck.deal_card())
    dealerhand.add_card(deck.deal_card())
    #print playerhand
    #print dealerhand
    
    in_play = True

def hit():
    global deck, playerhand,dealerhand, outcome, in_play, win, lost
    if in_play:
        # if the hand is in play, hit the player
        #if playerhand.get_value() < 21:
        playerhand.add_card(deck.deal_card())
        if playerhand.get_value() > 21:
            outcome = "You have busted!"
            lost += 1
            in_play = False
        
       

       
def stand():
    global deck, playerhand,dealerhand, outcome, in_play, win, lost
    if in_play:
        # if hand is in play, repeatedly hits the dealer until his hand has value 17 or more
        if playerhand.get_value()> 21:
            outcome = "You have busted!"
            lost += 1
        else:
            while dealerhand.get_value() < 17:
                dealerhand.add_card(deck.deal_card())
        
            if dealerhand.get_value() > 21:
                outcome = "You WON!"
                win += 1
            else:
                if dealerhand.get_value() >= playerhand.get_value():
                    outcome = "You Lost!"
                    lost += 1
                elif playerhand.get_value() <= 21:
                    outcome = "You WON!"
                    win += 1
    
    in_play = False
        
    #if outcome:
    #   print outcome
   

# draw handler    
def draw(canvas):
    #card = Card("S", "A")
    #card.draw(canvas, [300, 300])
    global deck, playerhand,dealerhand, outcome, in_play
    canvas.draw_text('Blackjack', (400, 570), 40, 'Black')
    playerhand.draw(canvas, [50, 400])
    dealerhand.draw(canvas, [50, 100])
    if in_play:
        canvas.draw_text("Hit or stand?", (350, 300), 30, 'Red')
        card_loc = CARD_BACK_CENTER
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [50 + CARD_CENTER[0], 100 + CARD_CENTER[1]], CARD_BACK_SIZE)
    else:
        canvas.draw_text("New deal?", (350, 300), 30, 'Red')
    
    canvas.draw_text(outcome, (350, 250), 30, 'Red')
    score = "score: " + str(win-lost)
    canvas.draw_text(score, (400, 50), 30, 'Black')


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()