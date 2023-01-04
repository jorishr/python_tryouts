num = int(122244)
counter = 0

while True:
    counter += 1
    inputNum = int(input('Guess the number between 0 and 1 000 000 000: '))
    if inputNum == num:
        print()
        print('You guessed correctly! The magic number is indeed', num)
        print('It took you', counter, 'attempt(s) to guess the answer!')
        break
    elif inputNum < 0:
        print('You entered a negative number! That\'s not how we play here. Goodbye')
        break
    elif inputNum > num:
      print('Too high, my friend! Try again...')
      print()
      continue
    else:
      print('Too low, my friend! Try again...')
      print()
      continue