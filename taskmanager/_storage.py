import _screen as scrn
import os, glob, time, datetime

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
    if debugMode:
      scrn.showTitle()
      time.sleep(1)
      message = scrn.makePretty('DEV_WARNING','DEBUG MODE = ON')
      print(f'\n{message}\n')
      time.sleep(1)
      message = scrn.makePretty('DEV_WARNING',f'Failed to load the existing task list.\n{e}\n\n\033[0;0mLoading program with empty task list...')
      print(f'\n{message}\n')
      time.sleep(10)
    data = []
    return data

def checkFolder(folder):
  entries = os.listdir('taskmanager')
  if folder in entries:
    return True
  return False


def getFileList():
  # returns list of backup files, most recently created first
  fileList = glob.glob('taskmanager/backup/*')
  if fileList:
    fileList.sort(key=os.path.getctime, reverse=True)
    return fileList
  fileList = []
  return fileList


def checkLimit(fileList):
  if len(fileList) >= 10:
    return True
  else: return False


def createDataBackup(data):
  existFolder = checkFolder('backup')
  if existFolder == False:
    os.mkdir('taskmanager/backup')
    createDataBackup(data)
  # only store max. 10 backup files; remove oldest first
  fileList = getFileList()
  limit = False
  if fileList:
    limit = checkLimit(fileList)
    if limit:
      os.remove(fileList[len(fileList) - 1])
    
  timestamp = datetime.datetime.now().replace(microsecond=0)
  hashed = hash(timestamp)
  name = f'taskmanager/backup/backup{hashed}.txt'
  storeDataInFile(data,name)


def loadBackupData():
  message = scrn.makePretty('DEFAULT','Searching for backup data...')
  print(f'\n{message}\n')
  try:
    fileList = getFileList()
    if fileList:
      mostRecent = fileList[0]
      message = scrn.makePretty('SUCCESS',f'Backup found.\nRestoring most recent backup: {mostRecent}')
      print(f'\n{message}')
      time.sleep(3)
      f = open(mostRecent, 'r')
      data = eval(f.read())
      f.close()
      message = scrn.makePretty('SUCCESS','Backup data restored successfully.')
      print(f'\n{message}')
      time.sleep(3)
      return data
    else:
      time.sleep(3)
      message = scrn.makePretty('USER_WARNING','No backup files found.')
      print(message)
      time.sleep(1)
      message = scrn.makePretty('USER_WARNING','Backup files should be placed in a folder named \'backup\'.\nExpected file name format: \'backup{hash of timestamp}.csv')
      print(f'\n{message}')
      time.sleep(10)
      data = []
      return data
  except Exception as e:
    if debugMode:
      message = scrn.makePretty('ERROR',f'Unable to load backup file:\n\n{e}')
      print(f'\n{message}')
      time.sleep(10)
    data = []
    return data