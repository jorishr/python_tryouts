import os, time

#subroutines to create game characters
def createChar(i):
  print('Player',i+1,'\n')
  charName = input('Write the name of your character.\n')
  print()
  charType = input('What type of character do you want to be? Human, imp, wizard, elf, orc, etc.\n')
  return charName, charType

def diceRoll(sides):
  import random
  result = random.randint(1,sides)
  return result

def generateHealthStats():
  diceSix = diceRoll(6)
  diceTwelve = diceRoll(12)
  charHealth = ((diceSix * diceTwelve) / 2) + 10
  #print('Health:',charHealth) 
  return charHealth
#generateHealthStats()

def generateStrengthStats():
  strengthStat = (generateHealthStats()) + 2
  #print('Strength:',strengthStat) 
  return strengthStat
#generateStrengthStats()

def printGameHeader():
  print('##############################\n')
  print('Welcome to...\n')
  print('Epic Fight of the Characters\n')
  print('##############################\n\n')

def printCharBuilderHeader():
  print('Build your characters!\n')
  print('----------------------\n')

# build the characters
printGameHeader()

def buildCharacters():
    for i in range(2):
        while True:
            printCharBuilderHeader()
            time.sleep(1)
            
            char = createChar(i)
            health = generateHealthStats()
            strength = generateStrengthStats()
            
            print('\nBuilding stats...\n')
            time.sleep(1)
            os.system('clear')
            
            printGameHeader()
            print('\nYou named your character:\n',char[0],'\n')
            print('Character type:\n',char[1],'\n')
            time.sleep(1)
            
            print('Character Stats')
            print('---------------')
            print('HEALTH:', health)
            print('STRENGTH:', strength,'\n')
            time.sleep(1)
            print('May your name go down in legend...')
            print('-----------------------------------\n\n')
            time.sleep(1)
    
            createNextChar = input('Happy with your stats? (y/n)\n')
            if createNextChar == 'y':
                num = i + 1
                globals()[f'player{num}'] = [char,health,strength] 
                os.system('clear')
                break
            else:
                time.sleep(1)
                os.system('clear')
                time.sleep(1)
                continue    

def calcStrengthDif(player1,player2):
    return abs(player1[2] - player2[2])

def calcPunishment(strengthDif):
    return (strengthDif + 1)

# battle game code subroutines
def printRulesOfTheGame(strengthDif,punishment):
    print('-----------------')
    print('RULES OF THE GAME\n')
    time.sleep(1)
    print(f'The difference in strength between the players is {strengthDif} points. The loser of each round will therefore receive a punishment of -{punishment} health points.\n')
    time.sleep(1)
    print('The first player to arrive at zero health status points, loses the game.')
    time.sleep(1)
    print('-----------------\n')
    input('Press any key to continue...')

def printBattleHeader(round):
  if round == 1:
    print('Let the battle begin!\n')
  else:
    print('Get ready for round',round,'...') 
  print('--------------------------\n')
  print('3...')
  time.sleep(1)
  print('2...')
  time.sleep(1)
  print('1...')
  time.sleep(1)
  print('Fight!\n')
  time.sleep(1)

def calcHealth(player1,player2,result,punishment,scoreP1,scoreP2,ties):
  if result == 1: #player1 won, punish player2 
    newHealth = player2[1] - punishment
    player2[1] = newHealth
    if newHealth <= 0:
      printGameOverMessage(player1,player2,result,scoreP1,scoreP2,ties)
      return 'gameover'
    return ''
  elif result == 2:
    newHealth = player1[1] - punishment
    player1[1] = newHealth
    if newHealth <= 0:
      printGameOverMessage(player1,player2,result,scoreP1,scoreP2,ties)
      return 'gameover'
    return ''
  else:
    return ''


def printGameOverMessage(player1,player2,result,scoreP1,scoreP2,ties):
    time.sleep(1)
    loser = ''
    if result == 1:
        loser  = player2[0][0]
        winner = player1[0][0]
    else:
        loser  = player1[0][0]
        winner = player2[0][0]
    print(f'GAME OVER! {loser} just died!\nRIP.\n\nCongratulations to {winner}, you are the winner of this Epic Battle of the Characters!\n')
    time.sleep(1)
    print('Final score:')
    print(f'Health {player1[0][0]}: {player1[1]}. | You won {scoreP1} round(s).')
    print(f'Health {player2[0][0]}: {player2[1]}. | You won {scoreP2} round(s).\n')
    print(ties,'rounds ended in a tie!\n\n\n')
    time.sleep(1)

def printBattleResult(player1,player2,result,attemptP1,attemptP2):
  print(f'Rolling the dice for {player1[0][0]}...\n')
  time.sleep(1)
  print(attemptP1,'\n')
  time.sleep(1)
  print(f'Rolling the dice for {player2[0][0]}...\n')
  time.sleep(1)
  print(attemptP2,'\n')
  time.sleep(1)
  if result == 1:
    print(f'{player1[0][0]} smashed {player2[0][0]}!\n')
  elif result == 2:
    print(f'{player2[0][0]} smashed {player1[0][0]}!\n')
  else:
    print('What a bummer, we have a tie!\n')

  print('-------------------------------\n')
  time.sleep(1)
  
def printHealthStatus(player1,player2,scoreP1,scoreP2):
  print(f'Health status for {player1[0][0]}: {player1[1]} | You won {scoreP1} round(s) so far.')
  print(f'Health status for {player2[0][0]}: {player2[1]} | You won {scoreP2} round(s) so far.')
  
def printPunishment(player1,player2,result,punishment,scoreP1,scoreP2):
  print('Time to punish...')
  time.sleep(1)
  if result == 1:
    print(f'{player2[0][0]} lost {punishment} health point(s)\n\n')
    printHealthStatus(player1,player2,scoreP1,scoreP2)
    time.sleep(1)
  elif result == 2:
    print(f'{player1[0][0]} lost {punishment} health point(s)\n\n')
    printHealthStatus(player1,player2,scoreP1,scoreP2)
    time.sleep(1)
  else:
    print('Just kidding...no loser this time.\n')
    printHealthStatus(player1,player2,scoreP1,scoreP2)
    time.sleep(1)
    return
    
def startBattle(player1,player2,punishment):
    os.system('clear')
    round = 0
    scoreP1 = 0
    scoreP2 = 0
    ties = 0

    while True:
        os.system('clear')
  
        round += 1
        printBattleHeader(round) 
  
        attemptP1 = diceRoll(6)
        attemptP2 = diceRoll(6)
        result = 0

        if attemptP1 > attemptP2:
            scoreP1 += 1
            result = 1
            printBattleResult(player1,player2,result,attemptP1,attemptP2)
            time.sleep(1)
            check = calcHealth(player1,player2,result,punishment,scoreP1,scoreP2,ties)
        elif attemptP1 < attemptP2:
            scoreP2 += 1
            result = 2
            printBattleResult(player1,player2,result,attemptP1,attemptP2)
            time.sleep(1)
            check = calcHealth(player1,player2,result,punishment,scoreP1,scoreP2,ties)
        else:
            #attemptP1 == attemptP2:
            result = 3
            ties += 1
            time.sleep(1)
            printBattleResult(player1,player2,result,attemptP1,attemptP2)
            check = ''

        if check == 'gameover':
            nextGame = input('Do you want to start a new game? (y/n):')
            if nextGame == 'y':
                os.system('clear')
                return True
            else:
                print('\n\n########################################')
                print('Thanks for playing! See you next time...')
                print('########################################')
                return False
        else: 
            printPunishment(player1,player2,result,punishment,scoreP1,scoreP2)
            time.sleep(5)
            print('\nGet ready for the next round...')
            time.sleep(1)
            continue

player1 = []
player2 = []
def startGame():
    newGame = True
    while newGame == True:
        buildCharacters()
        strengthDif = calcStrengthDif(player1,player2)
        punishment = calcPunishment(strengthDif)
        printRulesOfTheGame(strengthDif,punishment)
        newGame = startBattle(player1,player2,punishment)

startGame()