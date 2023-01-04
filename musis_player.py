from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False  # unpause the playback
  while True:
    print()
    print('##################')
    print('MyPod Music Player')
    print('##################')
    print()
    print('Enjoy the music...')
    print()
    stopPlayback = int(
      input('Press 2 to stop the playback and go back to the menu > '))
    if stopPlayback == 2:
      source.paused = True
      return  #function play() ends
    else:
      continue


while True:
  # clear the screen
  os.system('clear')
  # Show the menu
  print('##################')
  print('MyPod Music Player')
  print('##################')
  print()
  time.sleep(1)
  print('Press 1 to Play')
  time.sleep(1)
  print('Press 2 to Exit')
  print()
  time.sleep(1)
  print('Press anything else to see the menu again > ')

  userInput = input()
  if userInput == '1':
    print()
    print('#######################')
    print('Start loading some tunes...')
    time.sleep(1)
    os.system('clear')
    play()
  elif userInput == '2':
    break
  else:
    continue