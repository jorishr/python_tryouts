import os, time

def clear():
  os.system('clear')
  showTitle()


def pause():
  time.sleep(1)


def makePretty(type,message):
  if type.lower() == "success":
    return f'\033[032m{message}\033[0;0m'
  elif type.lower() == "error":
    return f'\033[031m[ERROR]: {message}\033[0;0m'
  elif type.lower() == "dev_warning":
    return f'\033[033m[WARNING]: {message}\033[0;0m'
  elif type.lower() == "user_warning":
    return f'\033[034m{message}\033[0;0m'
  else:
    return(f'\033[0;0m{message}\033[0;0m')


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


def getEditOptions(task):
  return makePretty('DEFAULT', f'\nWhat do you want to change about this task? (1-{len(task)})\n\n1. Description: {task[0]}\n2. Deadline: {task[1]}\n3. Priority: {task[2]}\n')


def getViewOptions():
  return makePretty('DEFAULT', f'What view do you want?\n\n * View all tasks (type \'all\')\n * View task by priority (type \'high/medium/low\)')