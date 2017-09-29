import random
player1 = 0
player2 = 0

# define random scoring function. either player1 gets the point or player2
def randomScore():
    global player1, player2
    x = random.randrange(0, 2)
    if x == 0:
        player1 += 1
    else:
        player2 += 1

#implementing scoring logic   
while not (((player1 >= 4) or (player2 >= 4)) and ((player1 - player2 > 1)or (player2 - player1 > 1))):
    
    randomScore()
    print(player1, player2)

    

