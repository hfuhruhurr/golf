N_PLAYERS = 6
N_DOWN_CARDS = 4
N_HOLES = 9
N_DECKS = 1

players = list(range(N_PLAYERS))

# initialize button to signify dealer
button = 0


def display():

    return 27


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
    