# py blackjack

# chip system ...

standard_deck = [
  "CAce","C2","C3","C4","C5","C6","C7","C8","C9","C10","CJack","CQueen","CKing",
  "DAce","D2","D3","D4","D5","D6","D7","D8","D9","D10","DJack","DQueen","DKing",
  "HAce","H2","H3","H4","H5","H6","H7","H8","H9","H10","HJack","HQueen","HKing",
  "SAce","S2","S3","S4","S5","S6","S7","S8","S9","S10","SJack","SQueen","SKing"
]

left_deck_player = standard_deck
left_deck_dealer = standard_deck

# win counter
player_wins = 0
dealer_wins = 0

def reset_decks():
  left_deck_player = standard_deck
  left_deck_dealer = standard_deck

reset_decks()
while winner = 0:
  #first cards
  new_card("dealer")
  new_card("player")
  
  #output player cards
  print("Your cards: \r")
  for card in player_cards:
    print(card + " \r")
  print("")
  print("Sum: " + value(player_cards)
  
  # player input to stand / hit / double
  choice = input("stand/hit/double > ")
        
  # if players cards value sum exceed 21 he lost
  if value(player_cards) > 21:
    winner = "dealer"
  
  # if dealers cards value sum exceed 21 he lost
  if value(dealer_cards) > 21:
    winner = "player"
  
  #check who has more value
  if value(player_cards) < 21 || value(dealer_cards) < 21 || value(player_cards) > value(dealer_cards):
    winner = "player"
    
  if value(player_cards) < 21 || value(dealer_cards) < 21 || value(player_cards) < value(dealer_cards):
    winner = "dealer"

  
def new_card(side):
  if side == "dealer":
    new_card = left_deck_dealer[random(0,left_deck_dealer.len()]
    left_deck_dealer.remove(new_card)
    dealer_cards.add(new_card)
                                       
  elif side == "player":
    new_card = left_deck_player[random(0,left_deck_player.len()]
    left_deck_player.remove(new_card)
    player_cards.add(new_card)

def value(list):
  value = 0
  for card in list:
    card = card[1:]
    if card == "Ace":
      value = value + 1             
    elif card == "Jack":
      value = value + 10             
    elif card == "Queen":
      value = value + 10             
    elif card == "King":
      value = value + 10
    else:
      value = value + int(card)
                                       
