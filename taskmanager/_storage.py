import _screen as scrn
import os, time, random

debugMode = True

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
    scrn.showTitle()
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