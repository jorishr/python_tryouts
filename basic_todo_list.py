myTodoList = []
title = 'My Todo List'
print(f'{title: ^35}', end='\n\n')

def printList(list):
  for i in list:
    print(i)


while True:
  action = input(
    'What do you want to do? View list, add item or remove item? Type (v/a/r)...\n\nType \'exit\' to leave the app.\n\n'
  )
  if action == 'v':
    printList(myTodoList)
    continue
  elif action == 'a':
    item = input('Enter a new task...\n\n')
    myTodoList.append(item)
    continue
  elif action == 'r':
    item = input('Enter the task to remove...\n\n')
    if item in myTodoList:
      myTodoList.remove(item)
      continue
    else:
      print('That task doesn\t exist')
      continue
  elif action == 'exit':
    break
  else:
    print('It did not recognize that command. Try again.')
    continue
