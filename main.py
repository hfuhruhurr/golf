import random 

N_PLAYERS = 6
N_DECKS = 1 
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
RANKS = ['A', '2']#, '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
SUITS = list('CDHS')
        
       
class Card():
    def __init__(self, deck_number, rank, suit):
        self.deck_number = deck_number
        self.rank = rank 
        self.suit = suit

    def __repr__(self):
        return f'Deck {self.deck_number}, {self.rank} of {self.suit}'
         

class Stack():
    def __init__(self):
        self.cards = []
        self.buildFreshStack()

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
    def __init__(self, seat_num: int, button: int):
        self.seat_num = seat_num 
        self.has_button = True if seat_num == button else False
        self.down_cards = []

    def __repr__(self):
        player_info = f'Player {self.seat_num}'
        button_info = 'has button' if self.has_button else 'nope' 
        return player_info + ': ' + button_info

    def addDownCard(self, down_card: Card):
        self.down_cards.append(down_card)


class Players():
    def __init__(self):
        self.button = 0
        self.roster = []
        self.buildRoster(N_PLAYERS, 0)
        
    def buildRoster(self, n_players, button):
        for i in range(n_players):
            self.roster.append(Player(i, button))
    
    def assignButton(self):
        return 27

    def showAllPlayers(self):
        for dude in self.roster:
            print(dude)


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

def deal_down_cards():
    

    return 27



# who's playing?
dudes = Players()

# well then get the cards
stack = Stack()

# friggin' deal already



# stack.showAllCards()
print('-'*80)
dudes.showAllPlayers()
