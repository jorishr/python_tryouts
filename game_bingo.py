import random, time, os

def getNum():
  num = random.randint(0,90)
  return num 

def generateBoard(boardNumList):  
  board = []

  print('Here are the numbers of your bingo card...')
  time.sleep(1)

  for i in range(0,8): 
    num = getNum()
    
    print(num)
    time.sleep(1)
    
    if num not in boardNumList:
      boardNumList.append(num)
      
  boardNumList.sort()
  row1 = [boardNumList[0], boardNumList[1], boardNumList[2]]
  board.append(row1)
  row2 = [boardNumList[3], 'BINGO', boardNumList[4]]
  board.append(row2)
  row3 = [boardNumList[5], boardNumList[6], boardNumList[7]]
  board.append(row3)
  return board, boardNumList
  
def printHeader():
  headerTxt = 'bingo card game'
  print('\033[0;34m', end='')
  print(f'{headerTxt.title():^33}', end='\n\n')
  print('\033[0;30m', end='')
  
def printPretty(board):
  print('\033[0;34m', end='')
  for row in board:
    print()
    print('---------------------------------')
    for item in row:
      if item == 'X' or item == 'BINGO':
        print(f'\033[0;36m{item:^10}\033[0;34m', end='|')
      else:
        print(f'{item:^10}', end='|')
  print('\n---------------------------------')

def game():
  boardNumList = []
  gameNumList = []
  
  printHeader()
  
  print('Generating new board...')
  time.sleep(1)
  
  game = generateBoard(boardNumList)
  bingoBoard = game[0]
  boardNumList = game[1]

  printPretty(bingoBoard)
  time.sleep(3)
  os.system('clear')
  
  while True:
    printHeader()
    time.sleep(1)
    printPretty(bingoBoard)
    time.sleep(1)
    print('\nGenerating new number...')
    time.sleep(1)
  
    gameNum = getNum()
    
    print(f'\nThe next number is...{gameNum}')
    time.sleep(1)
    
    if gameNum in boardNumList:
      print('\033[0;32mCool! You got one!')
      time.sleep(1)
      gameNumList.append(gameNum)
      for i in range(3):
        for j in range(3):
          if bingoBoard[i][j] == gameNum:
            bingoBoard[i][j] = 'X'
            break
      win = True
    else:
      time.sleep(1)
      print('\033[0;31mNo luck this time!')
      time.sleep(1)

    time.sleep(1)
    os.system('clear')
    
    if len(gameNumList) == 8:
      printHeader()
      printPretty(bingoBoard)
      winTxt = '\nBINGO! You won!'
      print('\033[0;36m', end='')
      print(f'{winTxt:^33}', end='\n\n')
      time.sleep(5)
      print('Thanks for playing and goodbye.')
      time.sleep(2)
      break

game()