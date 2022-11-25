from os import system
import time

class Game:
    """
    Game has 2 players.
    """
    def __init__(self,over = False,gameNum = 0,asum = 0,bsum = 0,amiscPoints = 0,bmiscPoints = 0,awin = 0,bwin = 0):
        self.gameNum = gameNum
        self.asum = asum
        self.bsum = bsum
        self.over = over
        self.amiscPoints = amiscPoints
        self.bmiscPoints = bmiscPoints
        self.awin = awin
        self.bwin = bwin

def display(player1,player2,game1,game2,game3,cycle):
    print "Game one:"
    print "                " + player1 + "           " + player2
    print "Hands won:        " + str(game1.awin) + "               " + str(game1.bwin)
    print "Score:           " + str(game1.asum + game1.amiscPoints) + "              " + str(game1.bsum + game1.bmiscPoints)
    if game1.over:
        print "Game over, ",
        if (game1.asum + game1.amiscPoints) > (game1.bsum + game1.bmiscPoints):
            print player1 + " won."
        else:
            print player2 + " won."
        
    print
    if cycle > 1:
        print "Game two:"
        print "                " + player1 + "           " + player2
        print "Hands won:        " + str(game2.awin) + "               " + str(game2.bwin)
        print "Score:           " + str(game2.asum + game2.amiscPoints) + "              " + str(game2.bsum + game2.bmiscPoints)
        if game2.over:
            print "Game over, ",
            if (game2.asum + game2.amiscPoints) > (game2.bsum + game2.bmiscPoints):
                print player1 + " won."
            else:
                print player2 + " won."
        print
        if cycle > 2:
            print "Game three:"
            print "                " + player1 + "           " + player2
            print "Hands won:        " + str(game3.awin) + "               " + str(game3.bwin)
            print "Score:           " + str(game3.asum + game3.amiscPoints) + "              " + str(game3.bsum + game3.bmiscPoints)
            if game3.over:
                print "Game over, ",
                if (game3.asum + game3.amiscPoints) > (game3.bsum + game3.bmiscPoints):
                    print player1 + " won."
                else:
                    print player2 + " won."
            print

def fix(player1,player2,game1,game2,game3):
    keepGo = True
    while keepGo:
        system('CLS')
        display(player1,player2,game1,game2,game3,3)
        print "Hand number: game1",game1.gameNum,"game2",game2.gameNum,"game3",game3.gameNum
        print "1. scores"
        print "2. win number"
        change = raw_input("What to change? or exit")
        if change == 'exit' or change == 'Exit' or change == 'EXIT':
            keepGo = False
        elif is_num(change):
            change = int(change)
            if change == 2:
                whatGame = raw_input("Which game?")
                if is_num(whatGame):
                    whatGame = int(whatGame)
                    if whatGame == 1:
                        whatPlayer = raw_input("What player?")
                        if is_num(whatPlayer):
                            whatPlayer = int(whatPlayer)
                            if whatPlayer == 1:
                                byWhat = raw_input("Change by What?")
                                if is_num(byWhat):
                                    game1.awin += int(byWhat)
                            elif whatPlayer == 2:
                                byWhat = raw_input("Change by What?")
                                if is_num(byWhat):
                                    game1.bwin += int(byWhat)
                    elif whatGame == 2:
                        whatPlayer = raw_input("What player?")
                        if is_num(whatPlayer):
                            whatPlayer = int(whatPlayer)
                            if whatPlayer == 1:
                                byWhat = raw_input("Change by What?")
                                if is_num(byWhat):
                                    game2.awin += int(byWhat)
                            elif whatPlayer == 2:
                                byWhat = raw_input("Change by What?")
                                if is_num(byWhat):
                                    game2.bwin += int(byWhat)
                    elif whatGame == 3:
                        whatPlayer = raw_input("What player?")
                        if is_num(whatPlayer):
                            whatPlayer = int(whatPlayer)
                            if whatPlayer == 1:
                                byWhat = raw_input("Change by What?")
                                if is_num(byWhat):
                                    game3.awin += int(byWhat)
                            elif whatPlayer == 2:
                                byWhat = raw_input("Change by What?")
                                if is_num(byWhat):
                                    game3.bwin += int(byWhat)
                        
            elif change == 1:
                print player1," Score:","game 1",game1.asum,"game 2",game2.asum,"game 3",game3.asum
                print player2," Score:","game 1",game1.bsum,"game 2",game2.bsum,"game 3",game3.bsum
                changeWhat = raw_input("What player's score should change? (1 or 2)")
                if is_num(changeWhat):
                    changeWhat = int(changeWhat)
                    if changeWhat == 1:
                        gameWhat = raw_input("What game?")
                        if is_num(gameWhat):
                            gameWhat = int(gameWhat)
                            if gameWhat == 1:
                                changeBy = raw_input("Change by what?")
                                if is_num(changeBy):
                                    game1.asum += int(changeBy)
                            elif gameWhat == 2:
                                changeBy = raw_input("Change by what?")
                                if is_num(changeBy):
                                    game2.asum += int(changeBy)
                            elif gameWhat == 3:
                                changeBy = raw_input("Change by what?")
                                if is_num(changeBy):
                                    game3.asum += int(changeBy)
                    elif changeWhat == 2:
                        gameWhat = raw_input("What game?")
                        if is_num(gameWhat):
                            gameWhat = int(gameWhat)
                            if gameWhat == 1:
                                changeBy = raw_input("Change by what?")
                                if is_num(changeBy):
                                    game1.bsum += int(changeBy)
                            elif gameWhat == 2:
                                changeBy = raw_input("Change by what?")
                                if is_num(changeBy):
                                    game2.bsum += int(changeBy)
                            elif gameWhat == 3:
                                changeBy = raw_input("Change by what?")
                                if is_num(changeBy):
                                    game3.bsum += int(changeBy)
                        

        
def play():
    system('CLS')
    gameOn = True
    print "Welcome to Ben's Gin Rummy score-keeper!\n"
    player1 = raw_input("What is player one's name?")
    player2 = raw_input("What is player two's name?")
    game1 = Game()
    game2 = Game()
    game3 = Game()
    system('CLS')
    cycle = 1
    #Undo Help
    #game1 stats
    g1asum = 0
    g1bsum = 0
    g1over = 0
    g1amiscPoints = 0
    g1bmiscPoints = 0
    g1awin = 0
    g1bwin = 0
    #game2 stats
    g2asum = 0
    g2bsum = 0
    g2over = 0
    g2amiscPoints = 0
    g2bmiscPoints = 0
    g2awin = 0
    g2bwin = 0
    #game3 stats
    g3asum = 0
    g3bsum = 0
    g3over = 0
    g3amiscPoints = 0
    g3bmiscPoints = 0
    g3awin = 0
    g3bwin = 0
    exitCommand = False
    while gameOn:
        display(player1,player2,game1,game2,game3,cycle)
        print "1 = " + player1
        print "2 = " + player2
        winner = raw_input("Who won? Enter 1 or 2 (or undo, rules, edit, restart, quit))\n")
        system('CLS')
        if winner == 'rules' or winner == 'Rules' or winner == 'RULES':
            instructions()
        elif winner == 'edit' or winner == 'Edit' or winner == 'EDIT':
            fix(player1,player2,game1,game2,game3)
        elif winner == 'restart' or winner == 'Restart' or winner == 'RESTART':
            system('CLS')
            restart = raw_input("Are you sure you want to restart and lose all data? (yes or no)\n")
            if restart == 'yes' or restart == 'YES' or restart == 'Yes' or restart == 'y' or restart == 'Y':
                return play()
        elif winner == 'quit' or winner == 'Quit' or winner == 'QUIT':
            system('CLS')
            end = raw_input("Are you sure you want to quit Grandma's Gin Rummy Score-Keeper? (yes or no)\n")
            if end == 'yes' or end == 'Yes' or end == 'YES' or end == 'Y' or end == 'y':
                exitCommand = True
                gameOn = False
        elif winner == 'undo' or winner == 'Undo' or winner == 'UNDO':
            game1.asum = g1asum
            game1.bsum = g1bsum
            game1.over = g1over
            game1.amiscPoints = g1amiscPoints
            game1.bmiscPoints = g1bmiscPoints
            game1.awin = g1awin
            game1.bwin = g1bwin

            game2.asum = g2asum
            game2.bsum = g2bsum
            game2.over = g2over
            game2.amiscPoints = g2amiscPoints
            game2.bmiscPoints = g2bmiscPoints
            game2.awin = g2awin
            game2.bwin = g2bwin

            game3.asum = g3asum
            game3.bsum = g3bsum
            game3.over = g3over
            game3.amiscPoints = g3amiscPoints
            game3.bmiscPoints = g3bmiscPoints
            game3.awin = g3awin
            game3.bwin = g3bwin
        elif is_num(winner):
            winner = int(winner)
            if winner == 1:
                howOut = winWay(player1)
                if howOut[0]:
                    (result,opposite) = scoreCalc(howOut,player2)
                    system('CLS')
                    if result:
                        #Undo Help
                        #game1 stats
                        g1asum = game1.asum
                        g1bsum = game1.bsum
                        g1over = game1.over
                        g1amiscPoints = game1.amiscPoints
                        g1bmiscPoints = game1.bmiscPoints
                        g1awin = game1.awin
                        g1bwin = game1.bwin
                        #game2 stats
                        g2asum = game2.asum
                        g2bsum = game2.bsum
                        g2over = game2.over
                        g2amiscPoints = game2.amiscPoints
                        g2bmiscPoints = game2.bmiscPoints
                        g2awin = game2.awin
                        g2bwin = game2.bwin
                        #game3 stats
                        g3asum = game3.asum
                        g3bsum = game3.bsum
                        g3over = game3.over
                        g3amiscPoints = game3.amiscPoints
                        g3bmiscPoints = game3.bmiscPoints
                        g3awin = game3.awin
                        g3bwin = game3.bwin
                        if not game1.over:
                            game1.gameNum += 1
                            if opposite:
                                game1.bsum += result
                                game1.bwin += 1
                            else:
                                game1.asum += result
                                game1.awin += 1
                        if not game2.over and (game1.awin > 1 or game1.over):
                            game2.gameNum += 1
                            if opposite:
                                game2.bsum += result
                                game2.bwin += 1
                            else:
                                game2.asum += result
                                game2.awin += 1
                        if not game3.over and (game2.awin > 1 or game2.over):
                            game3.gameNum += 1
                            if opposite:
                                game3.bsum += result
                                game3.bwin += 1
                            else:
                                game3.asum += result
                                game3.awin += 1
                    else:
                        system('CLS')
                else:
                    system('CLS')
            elif winner == 2:
                howOut = winWay(player2)
                if howOut[0]:
                    (result,opposite) = scoreCalc(howOut,player1)
                    system('CLS')
                    if result:
                        #Undo Help
                        #game1 stats
                        g1asum = game1.asum
                        g1bsum = game1.bsum
                        g1over = game1.over
                        g1amiscPoints = game1.amiscPoints
                        g1bmiscPoints = game1.bmiscPoints
                        g1awin = game1.awin
                        g1bwin = game1.bwin
                        #game2 stats
                        g2asum = game2.asum
                        g2bsum = game2.bsum
                        g2over = game2.over
                        g2amiscPoints = game2.amiscPoints
                        g2bmiscPoints = game2.bmiscPoints
                        g2awin = game2.awin
                        g2bwin = game2.bwin
                        #game3 stats
                        g3asum = game3.asum
                        g3bsum = game3.bsum
                        g3over = game3.over
                        g3amiscPoints = game3.amiscPoints
                        g3bmiscPoints = game3.bmiscPoints
                        g3awin = game3.awin
                        g3bwin = game3.bwin
                        if not game1.over:
                            game1.gameNum += 1
                            if opposite:
                                game1.asum += result
                                game1.awin += 1
                            else:
                                game1.bsum += result
                                game1.bwin += 1
                        if not game2.over and (game1.bwin > 1 or game1.over):
                            game2.gameNum += 1
                            if opposite:
                                game2.asum += result
                                game2.awin += 1
                            else:
                                game2.bsum += result
                                game2.bwin += 1
                        if not game3.over and (game2.bwin > 1 or game2.over):
                            game3.gameNum += 1
                            if opposite:
                                game3.asum += result
                                game3.awin += 1
                            else:
                                game3.bsum += result
                                game3.bwin += 1
                    else:
                        system('CLS')
                else:
                    system('CLS')
            
            else:
                system('CLS')
                print "Please choose integer from the list"
            if game2.awin >= 2 or game2.bwin >= 2 or game2.over:
                cycle = 3
            elif game1.awin >= 2 or game1.bwin >= 2 or game1.over:
                cycle = 2
        else:
            system('CLS')
            print "Please choose integer from the list"
        if not game1.over:
            if game1.asum >= 100 or game1.bsum >= 100:
                if game1.asum >= 100:
                    game1.amiscPoints += 100
                    if game1.awin - game1.bwin > 0:
                        game1.amiscPoints += 25 * (game1.awin - game1.bwin)
                else:
                    game1.bmiscPoints += 100
                    if game1.bwin - game1.awin > 0:
                        game1.bmiscPoints += 25 * (game1.bwin - game1.awin)
                game1.over = True
                if game1.bwin == game1.gameNum:
                    game1.bsum *= 2
                    print player2 + " schneidered " + player1 + "!"
                elif game1.awin == game1.gameNum:
                    game1.asum *= 2
                    print player1 + " schneidered " + player2 + "!"
        if not game2.over:
            if game2.asum >= 100 or game2.bsum >= 100:
                if game2.asum >= 100:
                    game2.amiscPoints += 100
                    if game2.awin - game2.bwin > 0:
                        game2.amiscPoints += 25 * (game2.awin - game2.bwin)
                else:
                    game2.bmiscPoints += 100
                    if game2.bwin - game2.awin > 0:
                        game2.bmiscPoints += 25 * (game2.bwin - game2.awin)
                game2.over = True
                if game2.bwin == game2.gameNum:
                    game2.bsum *= 2
                    print player2 + " schneidered " + player1 + "!"
                elif game2.awin == game2.gameNum:
                    game2.asum *= 2
                    print player1 + " schneidered " + player2 + "!"
        if not game3.over:
            if game3.asum >= 100 or game3.bsum >= 100:
                if game3.asum >= 100:
                    game3.amiscPoints += 100
                    if game3.awin - game3.bwin > 0:
                        game3.amiscPoints += 25 * (game3.awin - game3.bwin)
                else:
                    game3.bmiscPoints += 100
                    if game3.bwin - game3.awin > 0:
                        game3.bmiscPoints += 25 * (game3.bwin - game3.awin)
                game3.over = True
                if game3.bwin == game3.gameNum:
                    game3.bsum *= 2
                    print player2 + " schneidered " + player1 + "!"
                elif game3.awin == game3.gameNum:
                    game3.asum *= 2
                    print player1 + " schneidered " + player2 + "!"
        if game1.over and game2.over and game3.over:
            gameOn = False
    if not exitCommand:
        player1Tot = game1.asum + game1.amiscPoints + game2.asum + game2.amiscPoints + game3.asum + game3.amiscPoints
        player2Tot = game1.bsum + game1.bmiscPoints + game2.bsum + game2.bmiscPoints + game3.bsum + game3.bmiscPoints
        system('CLS')
        display(player1,player2,game1,game2,game3,cycle)
        print
        if player1Tot > player2Tot:
            print player1 + " wins the game with " + str(player1Tot) + " points!\n" + player2 + " lost with " + str(player2Tot) + " points."
        elif player2Tot > player1Tot:
            print player2 + " wins the game with " + str(player2Tot) + " points!\n" + player1 + " lost with " + str(player1Tot) + " points."
        again = raw_input("Would you like to play again? (yes or no)")
        if again == 'yes' or again == 'Yes' or again == 'YES':
            return play()
    
    print "Goodbye, please use again."
    time.sleep(.2)
    print "Written by Benjamin Brust with Python 2.7"
    print " 513 lines of code, released 12/27/2011"
    time.sleep(2)
    exit()

def scoreCalc(howOut,player):
    opposite = False
    while 1:
        caught = raw_input("How much was " + player + " caught with? or cancel\n")
        if is_num(caught) and int(caught) >= 0:
            caught = int(caught)
            if howOut[1]:
                caught -= howOut[1]
                if caught < 0:
                    caught = abs(caught)
                    opposite = True
                caught += 10
                
            else:
                caught += 25
            return caught,opposite
        elif caught == 'cancel' or caught == 'Cancel' or caught == 'CANCEL':
            return False,False
        else:
            system('CLS')
            print "Please choose positive integer"

def winWay(player):
    while 1:
        print "1 = gin"
        print "2 = knock"
        outWay = raw_input("How did " + player + " go out? or cancel\n")
        if is_num(outWay) and int(outWay) >= 1 and int(outWay) <= 2:
            outWay = int(outWay)
            if outWay == 1:
                return (outWay,0)
            elif outWay == 2:
                knock = raw_input("What did " + player + " knock on? or cancel\n")
                if is_num(knock):
                    knock = int(knock)
                    return (outWay,knock)
                elif knock == 'cancel' or knock == 'Cancel' or knock == 'CANCEL':
                    return (False,0)
            system('CLS')
        elif outWay == 'cancel' or outWay == 'Cancel' or outWay == 'CANCEL':
            return (False,0)
        else:
            system('CLS')
            print "Please choose integer from the list"

def is_num(string):
    """
    Tests a string to see if it is equal
    to a number.

    string -- string
    return -- boolean
    """
    try:
        float(string)
        return True
    except ValueError:
        return False

def instructions():
    system('CLS')
    print "Grandma's rules for rummy:"
    print "The winner gets 25 points for each of the loser's lost hands."
    print "The winner of a game gets 100 points."
    print "If the loser has won no hands in the game,\nthe winner's raw score is doubled."
    raw_input("Ready to play?")
    system('CLS')

play()


