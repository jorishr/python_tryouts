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
      print('\033[0;33mDEBUG MODE = ON')
      time.sleep(1)
      print(f'\nFailed to load the existing task list.\n{e}\n\n\033[0;0mLoading program with empty task list...')
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
  print('\033[0;0m\nSearching for backup data...')
  try:
    fileList = getFileList()
    if fileList:
      mostRecent = fileList[0]
      print(f'\n\033[0;32mBackup found.\nRestoring most recent backup: {mostRecent}')
      time.sleep(3)
      f = open(mostRecent, 'r')
      data = eval(f.read())
      f.close()
      print('\nBackup data restored successfully.')
      time.sleep(3)
      return data
    else:
      time.sleep(3)
      print('\n\033[0;33mNo backup files found.')
      print('\n\033[0;33mBackup files should be placed in a folder named \'backup\'.\nExpected file name format: \'backup{hash of timestamp}.csv')
      time.sleep(10)
      data = []
      return data
  except Exception as e:
    if debugMode:
      print(f'\n\033[0;31mUnable to load backup file:\n\n{e}')
      time.sleep(10)
    data = []
    return data