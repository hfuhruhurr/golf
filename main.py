import random 
from collections import Counter
import csv

N_PLAYERS = 6
N_DECKS = 1 
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
# RANKS = ['A', '2']#, '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
# SUITS = list('CDHS')
SUITS = ['\u2660', '\u2663', '\u2665', '\u2666']
N_DOWN_CARDS = 4
        
dude = {
'A': 1: 1,
'A': 2: 0,
'A': 3: 1,
'A': 4: -20
}       

print(dude)


# read in points.csv and populate in dict
with open('points.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = [row for row in reader]
    dude = {r['card']: [{k,v} for k,v in r.items() if 'card' not in k] for r in data}
    print(dude)

class Card():
    def __init__(self, deck_number, rank, suit):
        self.deck_number = deck_number
        self.rank = rank 
        self.suit = suit

    def __repr__(self):
        return f'{self.rank:>2}{self.suit}'
         

class Stack():
    def __init__(self):
        self.cards = []
        self.buildFreshStack()
        self.shuffle()

    def buildFreshStack(self):
        for deck in range(N_DECKS):
            for suit in SUITS:
                for rank in RANKS:
                    self.cards.append(Card(deck, rank, suit))

    def showAllCards(self):
        for card in self.cards:
            print(card)

    def shuffle(self):
        # for card nerds, this is a Fisher Yates shuffle
        # start at the last card
        # swap last card with random previous card
        # move up one card
        # repeat until done
        random.seed(27)
        for i in range(len(self.cards) - 1, 0, -1):                      # go to last unswapped card in deck
            r = random.randint(0, i)                                     # choose random card to swap with
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]  # swap cards

    def drawCard(self):
        return self.cards.pop()
    

class Player():
    def __init__(self, seat_num: int):
        self.seat_num = seat_num 
        self.has_button = False
        self.down_cards = []

    def __repr__(self):
        player_info = f'Player {self.seat_num}'
        button_info = 'has button ' if self.has_button else ' '*11 
        
        card_info = ''
        for card in self.down_cards:
            card_info += str(card) + ', '

        score_info = self.tallyScore()

        return player_info + ': ' + button_info + ': ' + card_info + '| ' #+ score_info

    def addDownCard(self, down_card: Card):
        self.down_cards.append(down_card)

    def tallyScore(self):
        # sort the ranks (to get ordinality)
        ranks = []
        for card in self.down_cards:
            ranks.append(card.rank)
        ranks.sort()

        # calculate ordinality
        c = Counter(ranks)
        print(c.items())

        # s = ''
        # for rank in ranks:
        #     s += rank 

        return 
    

class Players():
    def __init__(self):
        self.roster = []
        self.buildRoster(N_PLAYERS)
        self.button = None
        self.assignButton()

    def buildRoster(self, n_players):
        for i in range(n_players):
            self.roster.append(Player(i))
    
    def assignButton(self):
        if self.button is None:
            self.button = 0
        else:
            self.roster[self.button].has_button = False
            self.button = (self.button + 1) % N_PLAYERS
            
        self.roster[self.button].has_button = True
        return

    def showAllPlayers(self):
        for player in self.roster:
            print(player)

    def dealDownCards(self):
        for i in range(N_DOWN_CARDS):
            for j in range(1, N_PLAYERS + 1):
                player_to_be_dealt = (self.button + j) % N_PLAYERS
                self.roster[player_to_be_dealt].addDownCard(stack.drawCard())


def main():
    N_DOWN_CARDS = 4
    N_HOLES = 9
    N_DECKS = 1

    # initialize button to signify dealer
    button = 0
    
    for h in range(N_HOLES):
        print(f'HOLE {h+1}:')
        # STEP 0: ASSIGN DEALER
        dealer = players[button]
        print(f'  DEALER = Player {dealer}')

        # STEP 1: DEAL (dealer)

        # STEP 2: VIEW TWO DOWN CARDS (all players)

        # STEP 3: PLAYER TURN (4 turns per hole)
          # STEP 3A: ADD CARD
          # STEP 3B: DISCARD
          # STEP 3C: FLIP CARD

        # STEP 4: TALLY SCORE
        # STEP 5: GO TO NEXT HOLE
        button += 1 
        if button == N_PLAYERS:
            button = 0


# get the cards
stack = Stack()

# who's playing?
players = Players()

# friggin' deal already
players.dealDownCards()

print('-'*80)
players.showAllPlayers()
