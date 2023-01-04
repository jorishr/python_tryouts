from getpass import getpass as input

scoreP1 = 0
scoreP2 = 0
gameCounter = 0
inputErrorP1 = 'Player 1 entered an invalid option. Try again and enter r, p or s'
inputErrorP2 = 'Player 2 entered an invalid option. Try again and enter r, p or s'

print('#################################################')
print('Welcome to the famous rock, paper, scissors game!')
print('#################################################')
print()

while True:
  gameCounter += 1

  print('Round', gameCounter)
  print('#######')
  print()

  inputP1 = input('Player 1: Choose Rock (r), Paper (p) or Scissors(s)? ')
  print()
  inputP2 = input('Player 2: Rock (r), Paper (p) or Scissors(s)? ')
  print()
  
  if inputP1 == 'r':
    if inputP2 == 'r':
      print('Tie! You both picked rock')
    elif inputP2 == 'p':
      scoreP2 += 1
      print('Player 2 wins! Paper wins over rock.')
    elif inputP2 == 's':
      scoreP1 += 1
      print('Player 1 wins! Rock over scissors.')
    else:
     print(inputErrorP2)
     gameCounter -= 1
     continue
  elif inputP1 == 'p':
    if inputP2 =='r':
      scoreP2 += 1
      print('Player 1 wins! Paper wins against rock.')
    elif inputP2 == 'p':
      print('Tie! You both picked paper.')
    elif inputP2 == 's':
      scoreP2 += 1
      print('Player 2 wins. Scissors over paper.')
    else:
     print(inputErrorP2)
     gameCounter -= 1
     continue
  elif inputP1 == 's':
    if inputP2 == 'r':
      scoreP2 += 1
      print('Player 2 wins. Rock over scissors.')
    elif inputP2 == 'p':
      scoreP1 += 1
      print('Player 1 wins. Scissors over paper.')
    elif inputP2 == 's':
      print('Tie! You both picked scissors')
    else:
      print(inputErrorP2)
      gameCounter -= 1
      continue
  else:
    print(inputErrorP1)
    gameCounter -= 1
    continue
  if scoreP1 == 3:
    print()
    print('The game has ended. Player 1 was the first one to win three games out of the', gameCounter, 'rounds played')
    break
  elif scoreP2 == 3:
    print()
    print('The game has ended. Player 2 was the first one to win three games out of the', gameCounter, 'rounds played')
    print('Final score...', 'Player1:',scoreP1, 'Player2:', scoreP2)
    break
  else: 
    print()
    print()
    print('The score is... Player1:', scoreP1, '; Player2:', scoreP2)
    print()
    print('Next round!')
    print()
    continue