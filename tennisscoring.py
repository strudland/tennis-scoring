import random
player1 = 0
player2 = 0

#adding random points. either player1 gets the point or player2
def randomScore():
    global player1, player2
    x = random.randrange(0, 2)
    if x == 0:
        player1 += 1
    else:
        player2 += 1

def printScore(x, y):
    #define leading player
    if x > y: 
       leadplay = 'PLAYER 1'
    elif x < y:
        leadplay = 'PLAYER 2'
        
    #print(x,y) #remove hash before print function if u want to show scoring numbers
        
    #defining different possible states of game and printing result   
    if (x >= 3) or (y >= 3):
        if (abs(x - y) >= 2):
            print('WIN FOR '+leadplay)
        elif x == y:
            print('DEUCE') 
        elif (x < y) or (x > y):
            print('ADVANTAGE '+leadplay)
    else:
        if (player1 > player2):
            if x == 1 and y == 0:
                print('FIFTEEN - LOVE')
            if x == 2 and y == 0:
                print('THIRTY- LOVE')
            if x == 2 and y == 1:
                print('THIRTY - FIFTEEN')
        elif (player1 < player2):
            if x == 0 and y == 1:
                print('FIFTEEN - LOVE')
            if x == 0 and y == 2:
                print('THIRTY- LOVE')
            if x == 1 and y == 2:
                print('THIRTY - FIFTEEN')
        elif (player1 == player2):
            if x == 1 and y == 1:
                print('FIFTEEN - ALL')
            if x == 2 and y == 2:
                print('THIRTY- ALL')
    print('')
    

print('LOVE ALL \n')

#implementing scoring logic   
while not (((player1 >= 3) or (player2 >= 3)) and (abs(player1 - player2) >= 2)):
    randomScore()
    printScore(player1, player2)

    

