
# coding: utf-8

# In[1]:


import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True


# In[2]:


class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        pass
    
    def __str__(self):
        return (f'{self.rank} of {self.suit}')
        pass


# In[3]:


class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: "+deck_comp
        

    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card
        


# In[4]:


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def __str__(self):
        return str(self.cards)
    
    def add_card(self,card):
        #card passed in 
        #from Deck.deal()
        self.cards.append(card)
        self.value += values[card.rank]
        
        #track aces
        if card.rank == 'Ace':
            self.aces += 1
        
    
    def adjust_for_ace(self):
        #IF Total Value > 21 and I still have an ACE --> my Ace = 1
        while self.value>21 and self.aces:
            self.value -= 10
            self.aces -= 1
        


# In[5]:


class Chips:
    
    def __init__(self, total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
        
    
    def lose_bet(self):
        self.total -= self.bet
        


# In[6]:


def take_bet(chips):
    while True:
        try :
            chips.bet = int(input('How many chips would you like to bet? '))
        except:
            print('Sorry, a bet must be an integer!')
            continue
        else:
            if chips.bet > chips.total:
                print("Sorry, you don't have enough chips! You have: {}".format(chips.total))
            else :
                break


# In[7]:


def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


# In[8]:


def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x= input("Hit or Stand? Enter 'h' or 's' only : ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)
            break
        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            playing =False
            break
        else:
            print("Sorry, I don't understand that, Please enter 'h' or 's' only!!!")
            continue


# In[9]:


def show_some(player,dealer):
    print("Dealer's Hand :")
    print('one card hidden!')
    print(dealer.cards[1])
    print('\n')
    print('PLAYERS HAND: ')
    for card in player.cards:
        print(card)
    
def show_all(player,dealer):
    print('DEALERS HAND: ')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('PLAYERS HAND: ')
    for card in player.card:
        print(card)


# In[10]:


def player_busts(player, dealer, chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("PLAYER WINS! DEALER BUSTED!")
    chips.win_bet()
    
def dealer_wins(player,delaer,chips):
    print("DEALER WINS!")
    chips.lose_bet()
    
def push(player,dealer):
    print('Dealer and Player tie! PUSH')
    pass


# In[11]:


while True:
    #Print an opening statement
    print('Welcome to Blackjack! Get as close to 21 as you can without going over!')
    print('Dealer hits until she reaches 17. Aces count as 1 or 11')
    
    #Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
   
    #Set up the Player's chips
    player_chips = Chips()
    
    #Prompt the Player for their bet
    take_bet(player_chips)
        
    #Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)
    
    while playing: #recall this variable from our hit_or_stand function
        #Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        
        #Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        
        #If player's hand exceeds 21, run player_busts() and break out tof loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand,player_chips)
            break
        
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
        
        show_all(player_hand,dealer_hand)
        
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
            
    print('\n Player total chips are at:{}'.format(player_chips.total))
    
    new_game = input("Would you like to play another hand? y/n")
    
    if new_game[0].lower == 'y':
        playing = True
        continue
    else:
        print('Thank you for playing!')
        break
        

    
    

