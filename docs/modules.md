## Overview of commonly used Python Modules and Libraries
- [Overview of commonly used Python Modules and Libraries](#overview-of-commonly-used-python-modules-and-libraries)
  - [getpass](#getpass)
  - [os](#os)
  - [glob](#glob)
  - [argparse](#argparse)
  - [time, date and schedule](#time-date-and-schedule)
  - [random](#random)
  - [csv](#csv)
  - [json](#json)
  - [requests](#requests)
  - [bs4 web scraping](#bs4-web-scraping)

See [python modules documentation for further details](https://docs.python.org/3/py-modindex.html)

### getpass 
Hide terminal input from user
```python
from getpass import getpass as input
```
### os
Interact with the Operating System (terminal)
```python
import os
#clear terminal
os.system('clear')
os.popen('your terminal command')

path = os.path.join(f'{dirName}/', fileName) #join strings to create relative path
os.path.getctime #get the creation time of path or filename
```
### glob
The glob module finds all the path names matching a specified pattern.
```python
import glob
def getFileList():
  # returns list of backup files, most recently created first
  fileList = glob.glob('taskmanager/backup/*')
  if fileList:
    fileList.sort(key=os.path.getctime, reverse=True)
    return fileList
  fileList = []
  return fileList
```
### argparse
Argparse make processing command line arguments easier by reading the `sys.argv` and parsing those to your instructions. You also get a help menu and user friendly messages. 
- [doc](https://docs.python.org/3/library/argparse.html)
- [tutorial](https://docs.python.org/3/howto/argparse.html#)
```python
import argparse
# define the parser and run the command to parse the arguments given to the program from the command line
parser = argparse.ArgumentParser()
# add positional argument, type defaults is a str
parser.add_argument('arg1', help='msg1')
args = parser.parse_args() #the parser.parse_args() returns a namespace
print(args.arg1 + 'was used') 
# optional arguments, if argument is given args.debug = True; if not args.debug = None
parser.add_argument('-a', '--arg2', help='msg2', type=int, default=10)
parser.add_argument('-d','--debug', help='msg3', action='store_true')
print(args.arg2, args.debug, end='\n', sep=' | ')
```
### time, date and schedule
Control timing
```python
import time
#pause execution x seconds
print('Hello')
time.sleep(1)
print('World')

import datetime
today = datetime.date.today()
event = datetime.date(year=2023, month=1, day=10) # or ask for user input
print(event) #prints 2023-01-10
# once a date is properly formatted, you can use math functions
if today > event:
  print ('You missed that event')
#calculate the date in 30 days after today
difference = datetime.timedelta(days=30)
newDate = today + difference

# schedule a task to do something every x seconds
import schedule
def printMe():
  print("⏰")
schedule.every(2).seconds.do(printMe)
while True: 
  schedule.run_pending() 
  #runs any task in the schedule, resource intensive timeout to mitigate
  time.sleep(1)
```
### random 
Generate random numbers
```python
import random
num = random.randint(0,100)
```
### csv
```python
# See [documentation](https://docs.python.org/3/library/csv.html)
# working with Comma Separated Value files
import csv
# Check the actual data in the file and documentation first
# open a file that contains objects and use the DictReader method
with open('filename.extension') as file
  reader = csv.DictReader(file)

  total = 0
  for row in reader:
    #print('\t '.join(row))
    total += float(row['Cost']) * int(row['Amount'])
  return total
```
### json
```python
import json, requests
result = requests.get('api/endpoint')
user = result.json()
print(json.dump(user, indent=2)) # print pretty in console 
```
### requests
```python
import requests
result = requests.get('api/endpoint', headers={'Accept': 'application/json'})
if result.status_code == 200:
  user = result.json()
```
### bs4 web scraping
See [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)