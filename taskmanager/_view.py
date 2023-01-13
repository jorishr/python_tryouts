import _screen as scrn
import time

def showView(tasks,inputErrorMessage):
  scrn.clear()
  if len(tasks) == 0:
    print('Your task list is empty.\n')
    time.sleep(3)
  else:
    message = scrn.getViewOptions()
    userInput = input(f'\n{message}').lower().strip()

    if userInput[0:1] == 'a':
      scrn.clear()
      for task in tasks:
        print()
        for item in task:
          print(item, end=' | ')
    elif userInput[0:1] == 'h':
      scrn.clear()
      for task in tasks:
        print()
        if task[2] == 'high':
          for item in task:
            print(item, end=' | ')
    elif userInput[0:1] == 'm':
      scrn.clear()
      for task in tasks:
        print()
        if task[2] == 'medium':
          for item in task:
            print(item, end=' | ')
    elif userInput[0:1] == 'l':
      scrn.clear()
      for task in tasks:
        print()
        if task[2] == 'low':
          for item in task:
            print(item, end=' | ')
    else:
      scrn.clear()
      print(inputErrorMessage)

    userInput = input('\n\nDo you want to view something else? (y/n)\n\n')
    if userInput == 'y':
      scrn.clear()
      showView(tasks,inputErrorMessage)