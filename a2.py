#Vidit Jain
#2017370
#A2
from random import randint
player1=1
player2=2
tile1= 0
tile2= 0
tile3= 0
tile4= 0
tile5= 0
tile6= 0
tile7= 0
tile8= 0
tile9= 0
turn = player1

def validmove(move):
    """ Checks whether a move played by a player is valid or invalid.
        Return True if move is valid.
        
        A move is valid if the corresponding tile for the move is not ticked.
        """
    global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9,turn
    if move==1 and tile1==0:
        return True
    elif move==2 and tile2==0:
        return True
    elif move==3 and tile3==0:
        return True
    elif move==4 and tile4==0:
        return True
    elif move==5 and tile5==0:
        return True
    elif move==6 and tile6==0:
        return True
    elif move==7 and tile7==0:
        return True
    elif move==8 and tile8==0:
        return True
    elif move==9 and tile9==0:
        return True
    else:
        return False
def win():
    """ Returns True if the board state specifies a winning state for some player.
        
        A player wins if ticks made by the player are present either
        i) in a row
        ii) in a column
        iii) in a diagonal
        """
    global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9,turn
    if tile1==1 and tile2==1 and tile3==1:
        return True
    elif tile4==1 and tile5==1 and tile6==1:
        return True
    elif tile7==1 and tile8==1 and tile9==1:
        return True
    elif tile1==1 and tile4==1 and tile7==1:
        return True
    elif tile2==1 and tile5==1 and tile8==1:
        return True
    elif tile3==1 and tile6==1 and tile9==1:
        return True
    elif tile1==1 and tile5==1 and tile9==1:
        return True
    elif tile3==1 and tile5==1 and tile7==1:
        return True

    elif tile1==2 and tile2==2 and tile3==2:
        return True
    elif tile4==2 and tile5==2 and tile6==2:
        return True
    elif tile7==2 and tile8==2 and tile9==2:
        return True
    elif tile1==2 and tile4==2 and tile7==2:
        return True
    elif tile2==2 and tile5==2 and tile8==2:
        return True
    elif tile3==2 and tile6==2 and tile9==2:
        return True
    elif tile1==2 and tile5==2 and tile9==2:
        return True
    elif tile3==2 and tile5==2 and tile7==2:
        return True
    else:
        return False

def takeNaiveMove():
    """ Returns a tile number randomly from the set of unchecked tiles with uniform probability distribution.
        """
    global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9,turn
    move=randint(1,9)
    while not(validmove(move)):
        move=randint(1,9)
    return move
def takeStrategicMove():
    """ Returns a tile number from the set of unchecked tiles
        using some rules.
        
        """
    global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9,turn
    if turn==player1:
        #HORIZONTAL CHANCE
        if tile1==1 and tile2==1 and validmove(3):
            return 3
        elif tile2==1 and tile3==1 and validmove(1):
            return 1
        elif tile1==1 and tile3==1 and validmove(2):
            return 2
        elif tile4==1 and tile5==1 and validmove(6):
            return 6
        elif tile4==1 and tile6==1 and validmove(5):
            return 5
        elif tile5==1 and tile6==1 and validmove(4):
            return 4
        elif tile7==1 and tile8==1 and validmove(9):
            return 9
        elif tile7==1 and tile9==1 and validmove(8):
            return 8
        elif tile8==1 and tile9==1 and validmove(7):
            return 7

        #VERTICAL CHANCE
        elif tile1==1 and tile4==1 and validmove(7):
            return 7
        elif tile4==1 and tile7==1 and validmove(1):
            return 1
        elif tile1==1 and tile7==1 and validmove(4):
            return 4
        elif tile2==1 and tile5==1 and validmove(8):
            return 8
        elif tile2==1 and tile8==1 and validmove(5):
            return 5
        elif tile5==1 and tile8==1 and validmove(2):
            return 2
        elif tile3==1 and tile6==1 and validmove(9):
            return 9
        elif tile3==1 and tile9==1 and validmove(6):
            return 6
        elif tile6==1 and tile9==1 and validmove(3):
            return 3

        #DIAGONAL CHANCE
        elif tile1==1 and tile5==1 and validmove(9):
            return 9
        elif tile5==1 and tile9==1 and validmove(1):
            return 1
        elif tile1==1 and tile9==1 and validmove(5):
            return 5
        elif tile3==1 and tile5==1 and validmove(7):
            return 7
        elif tile3==1 and tile7==1 and validmove(5):
            return 5
        elif tile5==1 and tile7==1 and validmove(3):
            return 3

        #HORIZONTAL BLOCK
        elif tile1==2 and tile2==2 and validmove(3):
            return 3
        elif tile2==2 and tile3==2 and validmove(1):
            return 1
        elif tile1==2 and tile3==2 and validmove(2):
            return 2
        elif tile4==2 and tile5==2 and validmove(6):
            return 6
        elif tile4==2 and tile6==2 and validmove(5):
            return 5
        elif tile5==2 and tile6==2 and validmove(4):
            return 4
        elif tile7==2 and tile8==2 and validmove(9):
            return 9
        elif tile7==2 and tile9==2 and validmove(8):
            return 8
        elif tile8==2 and tile9==2 and validmove(7):
            return 7
        
        #VERTICAL BLOCK
        elif tile1==2 and tile4==2 and validmove(7):
            return 7
        elif tile4==2 and tile7==2 and validmove(1):
            return 1
        elif tile1==2 and tile7==2 and validmove(4):
            return 4
        elif tile2==2 and tile5==2 and validmove(8):
            return 8
        elif tile2==2 and tile8==2 and validmove(5):
            return 5
        elif tile5==2 and tile8==2 and validmove(2):
            return 2
        elif tile3==2 and tile6==2 and validmove(9):
            return 9
        elif tile3==2 and tile9==2 and validmove(6):
            return 6
        elif tile6==2 and tile9==2 and validmove(3):
            return 3

        #DIAGONAL BLOCK
        elif tile1==2 and tile5==2 and validmove(9):
            return 9
        elif tile5==2 and tile9==2 and validmove(1):
            return 1
        elif tile1==2 and tile9==2 and validmove(5):
            return 5
        elif tile3==2 and tile5==2 and validmove(7):
            return 7
        elif tile3==2 and tile7==2 and validmove(5):
            return 5
        elif tile5==2 and tile7==2 and validmove(3):
            return 3

        else:
            return takeNaiveMove()

    if turn==player2:

        #HORIZONTAL CHANCE
        if tile1==2 and tile2==2 and validmove(3):
            return 3
        elif tile2==2 and tile3==2 and validmove(1):
            return 1
        elif tile1==2 and tile3==2 and validmove(2):
            return 2
        elif tile4==2 and tile5==2 and validmove(6):
            return 6
        elif tile4==2 and tile6==2 and validmove(5):
            return 5
        elif tile5==2 and tile6==2 and validmove(4):
            return 4
        elif tile7==2 and tile8==2 and validmove(9):
            return 9
        elif tile7==2 and tile9==2 and validmove(8):
            return 8
        elif tile8==2 and tile9==2 and validmove(7):
            return 7
        
        #VERTICAL CHANCE
        elif tile1==2 and tile4==2 and validmove(7):
            return 7
        elif tile4==2 and tile7==2 and validmove(1):
            return 1
        elif tile1==2 and tile7==2 and validmove(4):
            return 4
        elif tile2==2 and tile5==2 and validmove(8):
            return 8
        elif tile2==2 and tile8==2 and validmove(5):
            return 5
        elif tile5==2 and tile8==2 and validmove(2):
            return 2
        elif tile3==2 and tile6==2 and validmove(9):
            return 9
        elif tile3==2 and tile9==2 and validmove(6):
            return 6
        elif tile6==2 and tile9==2 and validmove(3):
            return 3
        
        #DIAGONAL CHANCE
        elif tile1==2 and tile5==2 and validmove(9):
            return 9
        elif tile5==2 and tile9==2 and validmove(1):
            return 1
        elif tile1==2 and tile9==2 and validmove(5):
            return 5
        elif tile3==2 and tile5==2 and validmove(7):
            return 7
        elif tile3==2 and tile7==2 and validmove(5):
            return 5
        elif tile5==2 and tile7==2 and validmove(3):
            return 3

        #HORIZONTAL BLOCK
        elif tile1==1 and tile2==1 and validmove(3):
            return 3
        elif tile2==1 and tile3==1 and validmove(1):
            return 1
        elif tile1==1 and tile3==1 and validmove(2):
            return 2
        elif tile4==1 and tile5==1 and validmove(6):
            return 6
        elif tile4==1 and tile6==1 and validmove(5):
           return 5
        elif tile5==1 and tile6==1 and validmove(4):
            return 4
        elif tile7==1 and tile8==1 and validmove(9):
            return 9
        elif tile7==1 and tile9==1 and validmove(8):
            return 8
        elif tile8==1 and tile9==1 and validmove(7):
            return 7
        
        #VERTICAL BLOCK
        elif tile1==1 and tile4==1 and validmove(7):
            return 7
        elif tile4==1 and tile7==1 and validmove(1):
            return 1
        elif tile1==1 and tile7==1 and validmove(4):
            return 4
        elif tile2==1 and tile5==1 and validmove(8):
            return 8
        elif tile2==1 and tile8==1 and validmove(5):
            return 5
        elif tile5==1 and tile8==1 and validmove(2):
            return 2
        elif tile3==1 and tile6==1 and validmove(9):
            return 9
        elif tile3==1 and tile9==1 and validmove(6):
            return 6
        elif tile6==1 and tile9==1 and validmove(3):
            return 3
        
        #DIAGONAL BLOCK
        elif tile1==1 and tile5==1 and validmove(9):
            return 9
        elif tile5==1 and tile9==1 and validmove(1):
            return 1
        elif tile1==1 and tile9==1 and validmove(5):
            return 5
        elif tile3==1 and tile5==1 and validmove(7):
            return 7
        elif tile3==1 and tile7==1 and validmove(5):
            return 5
        elif tile5==1 and tile7==1 and validmove(3):
            return 3

        else:
            return takeNaiveMove()

def validBoard():
    """ Return True if board state is valid.
        
        A board state is valid if number of ticks by player1 is always either equal to or one more than the ticks by player2.
        """
    global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9,turn
    flag1=0
    flag2=0
    if tile1==1:
        flag1=flag1+1
    elif tile1==2:
        flag2=flag2+1
    elif tile2==1:
        flag1=flag1+1
    elif tile2==2:
        flag2=flag2+1
    elif tile3==1:
        flag1=flag1+1
    elif tile3==2:
        flag2=flag2+1
    elif tile4==1:
        flag1=flag1+1
    elif tile4==2:
        flag2=flag2+1
    elif tile5==1:
        flag1=flag1+1
    elif tile5==2:
        flag2=flag2+1
    elif tile6==1:
        flag1=flag1+1
    elif tile6==2:
        flag2=flag2+1
    elif tile7==1:
        flag1=flag1+1
    elif tile7==2:
        flag2=flag2+1
    elif tile8==1:
        flag1=flag1+1
    elif tile8==2:
        flag2=flag2+1
    elif flag1==flag2+1 or flag1==flag2:
        return True
    else:
        return False
def clearboard():
    global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9,turn
    tile1=tile2=tile3=tile4=tile5=tile6=tile7=tile8=tile9=0
def che1():
    global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9,turn
    if (tile1==1 and tile2==1 and tile3==1) or (tile4==1 and tile5==1 and tile6==1) or (tile7==1 and tile8==1 and tile9==1) or (tile1==1 and tile4==1 and tile7==1) or (tile2==1 and tile5==1 and tile8==1) or (tile3==1 and tile6==1 and tile9==1) or (tile1==1 and tile5==1 and tile9==1) or (tile3==1 and tile5==1 and tile7==1):
        return True
    else:
        return False
def che2():
    global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9,turn
    if (tile1==2 and tile2==2 and tile3==2) or (tile4==2 and tile5==2 and tile6==2) or (tile7==2 and tile8==2 and tile9==2) or (tile1==2 and tile4==2 and tile7==2) or (tile2==2 and tile5==2 and tile8==2) or (tile3==2 and tile6==2 and tile9==2) or (tile1==2 and tile5==2 and tile9==2) or (tile3==2 and tile5==2 and tile7==2):
        return True
    else:
        return False
def game(gametype=1):
    """ Returns 1 if player1 wins and 2 if player2 wins
        and 0 if it is a draw.
        
        gametype defines three types of games discussed above.
        i.e., game1, game2, game3
        """
    global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9,turn
    if gametype==1:
        for i in range(1,10):
            if i%2==1:
                n=takeNaiveMove()
                if n==1 and validmove(n):
                    tile1=1
                if n==2 and validmove(n):
                    tile2=1
                if n==3 and validmove(n):
                    tile3==1
                if n==4 and validmove(n):
                    tile4=1
                if n==5 and validmove(n):
                    tile5=1
                if n==6 and validmove(n):
                    tile6=1
                if n==7 and validmove(n):
                    tile7=1
                if n==8 and validmove(n):
                    tile8=1
                if n==9 and validmove(n):
                    tile9=1
            elif i%2==0:
                m=takeNaiveMove()
                if m==1 and validmove(m):
                    tile1=2
                if m==2 and validmove(m):
                    tile2=2
                if m==3 and validmove(m):
                    tile3=2
                if m==4 and validmove(m):
                    tile4=2
                if m==5 and validmove(m):
                    tile5=2
                if m==6 and validmove(m):
                    tile6=2
                if m==7 and validmove(m):
                    tile7=2
                if m==8 and validmove(m):
                    tile8=2
                if m==9 and validmove(m):
                    tile9=2
            if win():
                if che1():
                    clearboard()
                    return 1
                elif che2():
                    clearboard()
                    return 2
        if not win():
            clearboard()
            return 0
    if gametype==2:
        for i in range(1,10):
            if i%2==1:
                n=takeNaiveMove()
                if n==1 and validmove(n):
                    tile1=1
                if n==2 and validmove(n):
                    tile2=1
                if n==3 and validmove(n):
                    tile3==1
                if n==4 and validmove(n):
                    tile4=1
                if n==5 and validmove(n):
                    tile5=1
                if n==6 and validmove(n):
                    tile6=1
                if n==7 and validmove(n):
                    tile7=1
                if n==8 and validmove(n):
                    tile8=1
                if n==9 and validmove(n):
                    tile9=1
            elif i%2==0:
                m=takeStrategicMove()
                if m==1 and validmove(m):
                    tile1=2
                if m==2 and validmove(m):
                    tile2=2
                if m==3 and validmove(m):
                    tile3=2
                if m==4 and validmove(m):
                    tile4=2
                if m==5 and validmove(m):
                    tile5=2
                if m==6 and validmove(m):
                    tile6=2
                if m==7 and validmove(m):
                    tile7=2
                if m==8 and validmove(m):
                    tile8=2
                if m==9 and validmove(m):
                    tile9=2
            if win():
                if che1():
                    clearboard()
                    return 1
                elif che2():
                    clearboard()
                    return 2
        if not win():
            clearboard()
            return 0
                
    if gametype==3:
        for i in range(1,10):
            if i%2==1:
                turn=player1
                n=takeStrategicMove()
                if n==1 and validmove(1):
                    tile1=1
                if n==2 and validmove(2):
                    tile2=1
                if n==3 and validmove(3):
                    tile3==1
                if n==4 and validmove(4):
                    tile4=1
                if n==5 and validmove(5):
                    tile5=1
                if n==6 and validmove(6):
                    tile6=1
                if n==7 and validmove(7):
                    tile7=1
                if n==8 and validmove(8):
                    tile8=1
                if n==9 and validmove(9):
                    tile9=1
            elif i%2==0:
                turn=player2
                m=takeStrategicMove()
                if m==1 and validmove(1):
                    tile1=2
                if m==2 and validmove(2):
                    tile2=2
                if m==3 and validmove(3):
                    tile3=2
                if m==4 and validmove(4):
                    tile4=2
                if m==5 and validmove(5):
                    tile5=2
                if m==6 and validmove(6):
                    tile6=2
                if m==7 and validmove(7):
                    tile7=2
                if m==8 and validmove(8):
                    tile8=2
                if m==9 and validmove(9):
                    tile9=2
            if win():
                if che1():
                    clearboard()
                    return 1
                elif che2():
                    clearboard()
                    return 2
        if not win():
            clearboard()
            return 0
def game1(n):
    """ Returns the winning probability for player1.
        
        n games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.
        """
    count=0
    for i in range(n):
        if game(1)==1:
            count=count+1
    prob=count/n
    return prob
def game2(n):
    """Returns the winning probability for player1.
        
        n games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.
        """
    count=0
    for i in range(n):
        if game(2)==1:
            count=count+1
    prob=count/n
    return prob
def game3(n):
    """Returns the winning probability for player1. 
        
        n games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.
        """
    count=0
    for i in range(n):
        if game(3)==1:
            count=count+1
    prob=count/n
    return prob
