import os,time
import _screen as scrn
import _view as view
import _storage as storage

debugMode = True

def addTask(tasks):
  scrn.clear()
  desc = input('\nEnter a task description.\n').lower().strip()
  deadline = input('\nEnter a deadline.\n').lower().strip()
  priority = input(
    '\nEnter a priority level. (high, medium, low).\n').lower().strip()
  newTask = [desc, deadline, priority]
  tasks.append(newTask)

def removeTask(taskName,tasks):
  scrn.clear()
  if taskName == '':
    taskName = input('\nWhat task do you want to remove?\n').lower().strip()

  for task in tasks:
    if task[0] == taskName:
      tasks.remove(task)
      return True

  inputMessage = scrn.makePretty('USER_WARNING','That tasks does not exist. Try again or type \'cancel\' to go back to the menu')
  taskName = input(f'\n{inputMessage}\n') 
  if taskName.lower().strip()[0:1] != 'c':
    result = removeTask(taskName,tasks)
    return result
  return False

def editTask(taskName,tasks,inputErrorMessage):
  scrn.clear()
  if taskName == '':
    inputMessage = scrn.makePretty('DEFAULT', 'What task do you want to edit?')
    taskName = input(f'\n{inputMessage}\n').lower().strip()
  
  for task in tasks:
    if task[0] == taskName:
      inputMessage = scrn.getEditOptions(task)
      changeType = input(inputMessage)
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
  
  inputMessage = scrn.makePretty('USER_WARNING','That tasks does not exist. Try again or type \'cancel\' to go back to the menu')
  taskName = input(f'\n{inputMessage}\n')
  if taskName.lower().strip()[0:1] != 'c':
    result = editTask(taskName,tasks,inputErrorMessage)
    return result
  return False

def runTaskManager():
  tasks = storage.loadDataFromFile()
  menuOptions = ['add', 'view', 'edit', 'remove', 'create backup', 'restore backup', 'quit']
  inputErrorMessage = scrn.makePretty('USER_WARNING','Oops, I did not recognize that command. Try again.\n')

  while True:
    scrn.clear()
    scrn.showMenu(menuOptions)

    userAction = input(f'\nChoose an option from the menu (1-{len(menuOptions)})\n')
    
    if userAction == '1':
      addTask(tasks)
      message = scrn.makePretty('SUCCESS','Task added to the list. Back to the menu now...')
      print(f'\n{message}\n')
      time.sleep(2)
    elif userAction == '2':
      view.showView(tasks,inputErrorMessage)   
    elif userAction == '3':
      taskName = ''
      result = editTask(taskName,tasks,inputErrorMessage)
      if result == True:
        message = scrn.makePretty('SUCCESS','Task update completed. Back to the menu now...')
        print(f'\n{message}\n')
        time.sleep(2)
      else:
        continue
    elif userAction == '4':
      taskName = ''
      result = removeTask(taskName,tasks)
      if result == True:
        message = scrn.makePretty('SUCCESS','Task removed from the list. Back to the menu now...')
        print(f'\n{message}\n')
        time.sleep(2)
      else:
        continue
    elif userAction == '5':
      scrn.clear()
      print('Backing up your data...')
      time.sleep(2)
      storage.createDataBackup(tasks)
      message = scrn.makePretty('SUCCESS','Backup complete!')
      print(f'\n{message}\n')
      time.sleep(2)
    elif userAction == '6':
      tasks = storage.loadBackupData()
    elif userAction == '7':
      scrn.clear()
      print('Goodbye...')
      time.sleep(1)
      os.system('clear')
      exit()
    else:
      print(inputErrorMessage)
      time.sleep(2)
      continue  
    storage.storeDataInFile(tasks,'taskmanager/tasks.txt')
runTaskManager()