import os, time

def clear():
  os.system('clear')
  showTitle()

def pause():
  time.sleep(1)

def showTitle():
  titleTxt = '\033[0;34m=== \033[0;36mTask Manager \033[0;34m===\033[0;0m'
  print(f'{titleTxt:^35}', end='\n\n')

def showMenu(menuOptions):
  print('Menu')
  for i, item in enumerate(menuOptions):
    num = i + 1
    print(f'{num}. {item.capitalize()}')
    if i == 3 or i == 5:
      print('-----------------')