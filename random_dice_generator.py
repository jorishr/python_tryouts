def rollDice(size):
  import random
  num = random.randint(1,size)
  return num

def charHealth():
  diceSix = rollDice(6)
  diceEight = rollDice(8)
  charHealth = diceSix * diceEight
  return charHealth

print("Character stats generator")

while True:
  charName = input('What is the character\'s name? > ')
  getHealth = charHealth()
  print('The health of',charName,'is',getHealth)
  getMoreStats = input('Get stats for another character? y/n >')
  if getMoreStats == 'y':
    continue
  else:
    print('All done')
    break