from random import choice
loop = True
loop2 = True
wins = [0]*2
turn = -1
games = 0
cards = 1 #number of cards chosen at start
while loop2 == True: #loops through for each card
    while loop == True: #loops through games
        card0 = [0] * cards * 4 #makes an array of size 4 times cards which stores the starting cards
        for t in range(0,(cards*4)): #slects starting cards
            card0[t] = choice([i for i in range(1,52) if i not in card0])

        card1 = [0] * cards #makes an array of the size cards which stores the cards picked up each turn
        inplay = True
        while inplay == True: #loops through turns
            turn += 1
            for l in range(0,cards): #selects random cards for that turn
                card1[l] = choice([i for i in range(1,52) if i not in card1])
                
                
            matching = 0 #amount of cards matching
            for j in range(0,cards): #gets the ammount of matching cards
                for i in range(0,cards * 4):
                    if card1[j] == card0[i]:
                        for l in range(j+1,cards):
                            if card1[l]%13 == card0[j]%13: #checks to see if 2 or more cards in hand have the same face value if you do you've lost
                                matching -= 1
                                break
                        matching += 1
            if matching == cards: #adds a win if the amount of matching cards in equal to amount of cards needed
                 wins[turn % 2]+=1 #adds a win to the player based on that player 1 goes on every even turn
                 inplay = False
                 turn = -1
            card1.clear()
            card1 = [0] * cards
        games += 1
        card0.clear()
        card0 = [0] * cards * 4
        if games >= 100000: #Makes it so game repeats 100000 times
            loop = False
            cards += 1 #increases cards for next 100000 games
    games = 0
    loop = True
    player1w = wins[0] 
    player2w = wins[1]
    print(player1w,player2w) #outputes the amount of wins for player 1 and 2 for the last 10000 games
    wins[0] = 0
    wins[1] = 0
    if cards == 14: #stops loop once all 13 diffrenet amounts of cards have been tested
        loop2 = False 
