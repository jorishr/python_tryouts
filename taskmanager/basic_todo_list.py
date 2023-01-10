import os,time,random

debugMode = True

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

def addTask(tasks):
  clear()
  desc = input('\nEnter a task description.\n').lower().strip()
  deadline = input('\nEnter a deadline.\n').lower().strip()
  priority = input(
    '\nEnter a priority level. (high, medium, low).\n').lower().strip()
  newTask = [desc, deadline, priority]
  tasks.append(newTask)

def showView(tasks,inputErrorMessage):
  clear()
  userInput = input('\nWhat view do you want?\n\n * View all tasks(type \'all\')\n * View task by priority (type \'high/medium/low\')\n\n').lower().strip()
  if userInput[0:1] == 'a':
    clear()
    for task in tasks:
      print()
      for item in task:
        print(item, end=' | ')
  elif userInput[0:1] == 'h':
    clear()
    for task in tasks:
      print()
      if task[2] == 'high':
        for item in task:
          print(item, end=' | ')
  elif userInput[0:1] == 'm':
    clear()
    for task in tasks:
      print()
      if task[2] == 'medium':
        for item in task:
          print(item, end=' | ')
  elif userInput[0:1] == 'l':
    clear()
    for task in tasks:
      print()
      if task[2] == 'low':
        for item in task:
          print(item, end=' | ')
  else:
    clear()
    print(inputErrorMessage)

  userInput = input('\n\nDo you want to view something else? (y/n)\n\n')
  if userInput == 'y':
    clear()
    showView(tasks,inputErrorMessage)

def removeTask(taskName,tasks):
  clear()
  if taskName == '':
    taskName = input('\nWhat task do you want to remove?\n').lower().strip()

  for task in tasks:
    if task[0] == taskName:
      tasks.remove(task)
      return True

  taskName = input('\n\033[1;33mThat tasks does not exist. Try again or type \'cancel\' to go back to the menu\n\033[0;0m') 
  if taskName.lower().strip()[0:1] != 'c':
    result = removeTask(taskName,tasks)
    return result

  return False

def editTask(taskName,tasks,inputErrorMessage):
  clear()
  if taskName == '':
    taskName = input('\nWhat task do you want to edit?\n').lower().strip()
  
  for task in tasks:
    if task[0] == taskName:
      changeType = input(f'\nWhat do you want to change about this task? (1-{len(task)})\n\n1. Description: {task[0]}\n2. Deadline: {task[1]}\n3. Priority: {task[2]}\n')
      if changeType == '1':
        newName = input('\nEnter the new task description.\n').lower().strip()
        task[0] = newName
      elif changeType == '2':
        newDeadline = input('\nEnter the new deadline for the task.\n').lower().strip()
        task[1] = newDeadline
      elif changeType == '3':
        newPriority = input('\nEnter the new priority (high/medium/low)).\n').lower().strip()
        task[2] = newPriority
      else:
        print(inputErrorMessage)
        time.sleep(2)
        result = editTask(taskName,tasks,inputErrorMessage)
        return result
      return True

  taskName = input('\n\033[1;33mThat tasks does not exist. Try again or type \'cancel\' to go back to the menu\n\033[0;0m')
  if taskName.lower().strip()[0:1] != 'c':
    result = editTask(taskName,tasks,inputErrorMessage)
    return result
  
  return False

def storeDataInFile(data,name):
  f = open(name, 'w')
  f.write(f'{data}\n')
  f.close()

def loadDataFromFile():
  try:
    f = open('taskmanager/tasks.txt', 'r')
    data = eval(f.read())
    f.close()
    return data    
  except Exception as e:
    showTitle()
    print('\033[0;31mOops! Failed to load the existing task list.\n')
    time.sleep(2)
    if debugMode:
      print('\033[0;33mDEBUG MODE = ON\033[0;31m')
      time.sleep(1)
      print(e)
      print('\n\033[0;33mThe app will now run the program with some arbitrary data that was given to it by a clever developer...')
      time.sleep(10)
    data = [['work', 'tomorrow', 'high'], ['play', 'in two days', 'low']]
    return data

def createDataBackup(data):
  files = os.listdir('taskmanager')
  if 'backup' in files:
    name = f'taskmanager/backup/backup{random.randint(10000,99000)}.txt'
    storeDataInFile(data,name)
  else:
    os.mkdir('taskmanager/backup')
    createDataBackup(data)

def runTaskManager():
  tasks = loadDataFromFile()
  menuOptions = ['add', 'view', 'edit', 'remove', 'quit']
  inputErrorMessage = '\n\033[0;31mOops, I did not recognize that command. Try again.\n\033[0;0m'

  while True:
    clear()
    showTitle()
    showMenu(menuOptions)

    userAction = input(f'\nChoose an option from the menu (1-{len(menuOptions)})\n')
    
    if userAction == '1':
      addTask(tasks)
      print('\n\033[0;32mTask added to the list. Back to the menu now...\033[0;0m\n')
      time.sleep(2)
    elif userAction == '2':
      showView(tasks,inputErrorMessage)   
    elif userAction == '3':
      taskName = ''
      result = editTask(taskName,tasks,inputErrorMessage)
      if result == True:
        print('\n\033[0;32mTask update completed. Back to the menu now...\033[0;0m\n')
        time.sleep(2)
      else:
        continue
    elif userAction == '4':
      taskName = ''
      result = removeTask(taskName,tasks)
      if result == True:
        print('\n\033[0;32mTask removed from the list. Back to the menu now...\033[0;0m\n')
        time.sleep(2)
      else:
        continue
    elif userAction == '5':
      clear()
      print('Backing up your data...')
      createDataBackup(tasks)
      clear()
      exit()
    else:
      print(inputErrorMessage)
      time.sleep(2)
      continue  
    storeDataInFile(tasks,'taskmanager/tasks.txt')
runTaskManager()