inputNum = int(input('Enter a number to multiply between 2 and 100 > '))
score = 0
for i in range(1, 11, 1):
    print(i, 'x', inputNum, '= ? ')
    answer = int(input(''))
    if answer == i * inputNum:
        print(i, 'x', inputNum, '=', (i * inputNum))
        print('Well done!')
        score += 1
    else:
        print('Wrong answer!')
        print('The correct answer was', i * inputNum)
        print('Let\'s move to the next one...')
print('You scored', score, 'out of 10')