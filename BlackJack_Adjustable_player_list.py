#A Game of BlackJack
#Eventually make it dynamic so you can adjust the number of players
#then add in being able to adjust the bets
#enter 5 to 7 players, Progression: allow user to enter number of players and players left over that need to fill the table
#can be AI

#progression: shuffle Multiple Decks together

#progression: Allow for bets

#Rules:
#Player Competes aganist dealer
#dealer draws until dealer hits 17 or higher
#dealer must draw on a soft 17
#for every card player draws, dealer must also draw a card.


import random
#card_num = 51
#suits = ['hearts','clubs','spades','diamonds']          #create a list holding suits
deck = []
temp = 0
rand = 0
card_count = 0
players = []

print("Welcome to Black Jack in Python.")
num_players = int(input("Enter the number of players in the game, (5-7): "))
print("The Dealer will shuffle the deck and deal two cards to each player.")


def player_gen(num_players):
    "This function generates all the players that were entered in the"
    "begining of the game."

    for _ in range(num_players):
        players.append([f'Player {_ + 1}'])
    #print("Here is the output of the player generator function")
    #print(players)

    
player_gen(num_players)                                 #create a player generator function

for i in range(52):
    deck.append([i])
    i += 1                          #investigate if you need thi piece later
for _ in range(52):                                     #write suits into a list of list(array) that holds all 
    if (_/13)<1:                                       #all information about the cards, deck value, suit value
        deck[_].append('Hearts')                        #and face value
    elif (_/13)<2:
        deck[_].append('Clubs')
    elif (_/13)<3:
        deck[_].append('Spades')
    elif (_/13)<4:
        deck[_].append('Diamonds')
for _ in range(52):
    if _%13==0:
        deck[_].append('Ace')
    elif _%13==10:
        deck[_].append('Jack')
    elif _%13==11:
        deck[_].append('Queen')
    elif _%13==12:
        deck[_].append('King')
    else:
        deck[_].append(_%13+1)
i=0
#for i in range(52):                                #for loop to check that deck was created correctly
#    print(deck[i])

#shuffle deck i=0
for _ in  range(52):                                    #for loop to shuffle deck
    rand        = (int(random.random()*10)%52)          #seed random number from system time
    temp        = deck[_]
    deck[_]     = deck[rand]
    deck[rand]  = temp


    

def hand_value_2(hand):
    "This function is passed a list containing the player's hand"
    "and the value of that hand is evaluated"

    ace_holder = []             #initalize an empty list to hold the amount of ace value's a player can have.
                                #total amount of ace values is 4, write decsion tree accordingly

    score_pre_eval = 0
    ace_value = 0               #ace_value needs to be initalized to zero in the case that hand has no aces in it
   # for _ in range(1,len(hand)):   #test loop to see how to index corretly
   #     print(hand[_][2])

    
    
    for _ in range(1,len(hand)):                      #Evaluate the cards in the hand, evaluate the value of all non-ace's
        if hand[_][2] == 'Ace':               #place all aces into list ace_holder in order that their values you may 
            ace_holder.append(_)        #be evaluated in relation to the other cards in the hand
        elif hand[_][2] == 'Jack' or hand[_][2] == 'Queen' or hand[_][2] == 'King':
            score_pre_eval += 10
        else:
            score_pre_eval += hand[_][2]
    
    
    if len(ace_holder) == 1:            #Evaluate the cards in ace_holder based off
        if score_pre_eval <= 10:        #how many aces you have and the value of the other cards in the hand
            ace_value += 11
        elif score_pre_eval > 10:
            ace_value += 1
    elif len(ace_holder) == 2:
        if score_pre_eval <= 9:
            ace_value += 12
        elif score_pre_eval > 9:
            ace_value += 2
    elif len(ace_holder) == 3:
        if score_pre_eval <= 8:
            ace_value += 13
        elif score_pre_eval > 8:
            ace_value += 3
    elif len(ace_holder) == 4:
        if score_pre_eval <= 7:
            ace_value += 14
        elif score_pre_eval > 7:
            ace_value += 14
    else:
        pass

    score = score_pre_eval + ace_value
#    score = 0
    return score

def dealer_hand_value(hand):                       #make special function to evaluate dealer draw at the end of the game.
    "This function is passed a list containing the Dealer's hand"
    "and the value of that hand is evaluate"
    "Hand is also evaluated if it is a soft seventeen"
    "if it is a soft seventeen then another card must be drawn."

    ace_holder = []             #initalize an empty list to hold the amount of ace value's a player can have.
                                #total amount of ace values is 4, write decsion tree accordingly
    

    score_pre_eval = 0
    ace_value = 0               #ace_value needs to be initalized to zero in the case that hand has no aces in it
    #soft_ace = 'n'                      #soft_ace needs to be 
    
    for _ in hand:                      #Evaluate the cards in the hand, evaluate the value of all non-ace's
        if _[2] == 'Ace':               #place all aces into list ace_holder in order that their values may 
            ace_holder.append(_)        #be evaluated in relation to the other cards in the hand
        elif _[2] == 'Jack' or _[2] == 'Queen' or _[2] == 'King':
            score_pre_eval += 10
        else:
            score_pre_eval += _[2]
    
    
    if len(ace_holder) == 1:            #Evaluate the cards in ace_holder based off
        if score_pre_eval <= 10:        #how many aces you have and the value of the other cards in the hand
            ace_value += 11
            soft_ace = 'y'
        elif score_pre_eval > 10:
            ace_value += 1
            soft_ace = 'n'
    elif len(ace_holder) == 0:
        soft_ace = 'n'
    elif len(ace_holder) == 2:
        if score_pre_eval <= 9:
            ace_value += 12
            soft_ace = 'y'
        elif score_pre_eval > 9:
            ace_value += 2
            soft_ace = 'n'
    elif len(ace_holder) == 3:
        if score_pre_eval <= 8:
            ace_value += 13
            soft_ace= 'y'
        elif score_pre_eval > 8:
            ace_value += 3
            soft_ace = 'n'
    elif len(ace_holder) == 4:
        if score_pre_eval <= 7:
            ace_value += 14
            soft_ace = 'y'
        elif score_pre_eval > 7:
            ace_value += 4
            soft_ace = 'n'
    else:
        pass

    score = score_pre_eval + ace_value
    dealer_hvalue = [score,soft_ace]
    return dealer_hvalue                                        #Function returns the score of the hand and wether or not
                                                                #the deal holds a soft ace or not.

 

def game_eval(player1_score,dealer_score):
    "This function evaluates who one the game"
    if player1_score > dealer_score and player1_score < 21:
    #if player1_score > 21:                                     this function can be compressed with nested if loops at a later day.
            #(print
        print("Player One has Won the Game!")
        
    elif dealer_score > player1_score and dealer_score < 21:        #this will need to be rewriten to compare all player values
        print("The Dealer has Won the Game!")                       #in relation to one another.
    elif dealer_score == player1_score and player1_score < 21:      #easiest way will be to select the highest value 
        print("Player One and the Dealer have Tied the Game!")      # less than or equal to twenty one and select that 
    elif player1_score > 21 and dealer_score > 21:                  # players hand to be compared aganist the dealers 
        print("Both Player One and the Dealer Bust")                #hand
    elif player1_score == 21 and dealer_score != 21:
        print("Player One has Won the Game!")
    elif dealer_score == 21 and player1_score != 21:
        print("The Dealer has Won the Game!")
    elif dealer_score > 21 and player1_score <= 21:
        print("Player One has Won the Game!")
    elif player1_score > 21 and dealer_score <= 21:
        print("The Dealer has Won the Game!")



#player1_hand = []                                        #Value of player 1's hand
dealer_hand = []                                        #value of player 2's hand

#deal cards
for _ in range(2):
    dealer_hand.append(deck[card_count])
    card_count += 1
    for i in range(num_players):
        players[i].append(deck[card_count])
        card_count += 1

#print(players)

print(f"The Dealer's hand is {dealer_hand[0][2]} of {dealer_hand[0][1]} and {dealer_hand[1][2]} of {dealer_hand[1][1]}.")

for _ in range(num_players):
    print(f"{players[_][0]}'s hand consists of {players[_][1][2]} of {players[_][1][1]} and the {players[_][2][2]} of {players[_][2][1]}.")


#evaluate the value of each player's hand:

for _ in range(num_players):
    #print(players[_])
    score = hand_value_2(players[_])
    print(f"{players[_][0]}'s score is {score}")


#print(f"Player One's hand is {player1_hand[0][2]} of {player1_hand[0][1]} and {player1_hand[1][2]} of {player1_hand[1][1]}.")
#print(f"The Dealer's hand is {dealer_hand[0][2]} of {dealer_hand[0][1]} and {dealer_hand[1][2]} of {dealer_hand[1][1]}.")


#player1_score = hand_value_2(player1_hand)             #hand score for hand_value function
#dealer_score = dealer_hand_value(dealer_hand)[0]
#soft_ace_o = dealer_hand_value(dealer_hand)[1]


#print(f"The value of Player One's hand is {player1_score}")
#print(f"The value of The Dealer's hand is {dealer_score}")



#while player1_score < 21 and dealer_score <= 21:                           #while loop to allow player 1 to draw cards until they stay or bust
#    hit_stay_p1 = input("Player One would you like to Hit or Stay, (H/S)?: ")                   #code block must have if statment to exit loop for stay option (While statement does not evaluate until code block has completed)
#    if hit_stay_p1 == 'S' or hit_stay_p1 == 's':
#        print("Stay!")
#        print(f"Player One's Score remains: {player1_score}")
#        break
#    else:
#        print("Hit!")
#    player1_hand.append(deck[card_count])
#    card_count += 1
#    print(f"Player One's new card is: {player1_hand[2][2]} of {player1_hand[2][1]}")
#    player1_score = hand_value_2(player1_hand)                #Evaluate the new score for player one after they draw#
#    print(f"Player One's new Score is: {player1_score}")    #Evaluate wether player one has lost or not.
#    if player1_score > 21:                                  #Declare a Bust if Player One Bust
#        print("Player One Busts")
#        break
#    if player1_score == 21:
#        break
 #   dealer_hand.append(deck[card_count])
  #  card_count += 1
#    print(f"The Dealer's new card is: {dealer_hand[2][2]} of {dealer_hand[2][1]}")
#    dealer_hvalue = dealer_hand_value(dealer_hand)            #all of the dealer's hands must be evaluated in dealer_hand_value
#    dealer_score = dealer_hvalue[0]                          #from that function it willl be determined wether the dealer's hand is soft or not
#    soft_ace = dealer_hvalue[1]
#    print(f"soft_ace : {soft_ace}")
#    print(f"The Dealer's new score is: {dealer_score}") 
#    if dealer_score > 21:
#        print("The Dealer Busts!")

#must write program so that it has a soft ace outside of the function of dealer hand evaluation
#dealer must draw to 17 or higher and must draw on a soft 17
#write in an exit on this function if Player One Bust
#while dealer_score <= 17 or soft_ace_o == 'y':
#    print("Dealer must draw a new card")
#    dealer_hand.append(deck[card_count])
#    card_count += 1
#    dealer_hvalue = dealer_hand_value(dealer_hand)
#    dealer_score = dealer_hvalue[0]
#    soft_ace_o = dealer_hvalue[1]
#    temp_new_card = dealer_hand[-1]
#    print(f"Dealer's new card is {temp_new_card[2]} of {temp_new_card[1]}")                            #make sure indexing on this is correct for finding the last value in a list
#    print(f"Dealer's new score is: {dealer_score}")
 #   if dealer_hvalue[1] == 'y':
#        print("Dealer's hand is soft")
#    else:
#        break
        

#game_eval(player1_score,dealer_score)                      #Evaluate the game and show who one the game.    
