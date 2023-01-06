import os, time

myTodoList = []

def printHeader():
  title = 'My Todo List'
  print(f'{title: ^35}', end='\n\n')
  time.sleep(1)


def printList(list):
  print('\nList of tasks:\n')
  for i in range(len(list)):
    num = i + 1
    print(f'{num}. {list[i]}')
  print('---------------\n')


def printMenu():
  menuOptions = [
    'View list', 'Add item', 'Remove item', 'Edit item', 'Erase list'
  ]
  print('What do you want to do?', end='\n\n')
  for i in range(len(menuOptions)):
    num = i + 1
    print(f'{num}. {menuOptions[i]}', end='\n')


def getUserInput():
  time.sleep(1)
  userInput = input(
    '\nChoose a number from the menu or type \'exit\' to leave the app.\n\n')
  return userInput


def restart():
  time.sleep(1.5)
  os.system('clear')
  printHeader()
  printMenu()


def appendItem():
  item = input('\nPlease enter a new task...\n\n')
  isDuplicate = isItemInList(item)
  if isDuplicate == True:
    print('\nSorry, that task already exists. No duplicates allowed.')
    restart()
  else:
    myTodoList.append(item)
    print('\nItem added to the list')
    restart()


def editItem():
  item = input('\nEnter the task to edit...\n\n')
  checkItem = isItemInList(item)
  if checkItem == True:
    newInput = input(
      f'\nFound the task: {item}. Now write the new text for this task:\n')
    for i in range(len(myTodoList)):
      if myTodoList[i] == item:
        myTodoList[i] = newInput
        print('\nTask update completed.')
        restart()
  else:
    print('Sorry, item not found in the list.')
    restart()

def removeItem():
  item = input('\nEnter the task to remove...\n\n')
  checkItem = isItemInList(item)
  if checkItem == True:
    askConfirm = input(f'\nAre you sure you want to delete {item}? (y/n)\n')
    if askConfirm == 'y':
      myTodoList.remove(item)
      print(f'{item} removed from list.\n')
      restart()
    else:
      restart()
  else:
    print('\nSorry, that task doesn\'t exist')
    removeItem()


def clearList():
  askConf = askConfirm()
  if askConf == True:
    globals()['myTodoList'] = []
  restart()


def isItemInList(item):
  if item in myTodoList:
    return True
  return False


def askConfirm():
  answer = input('\nAre you sure? This action cannot be undone! (y/n)\n')
  if answer == 'y':
    return True
  return False

def startApp():
  printHeader()
  printMenu()

  while True:
    action = getUserInput()
    if action == '1':
      printList(myTodoList)
    elif action == '2':
      appendItem()
    elif action == '3':
      removeItem()
    elif action == '4':
      editItem()
    elif action == '5':
      clearList()
    elif action == 'exit':
      print('\nGoodbye!')
      time.sleep(1)
      os.system('clear')
      break
    else:
      print('\nI did not recognize that command. Try again.\n')
      restart()
startApp()