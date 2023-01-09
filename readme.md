# Python references
- [Python references](#python-references)
  - [Overview commonly used subroutines](#overview-commonly-used-subroutines)
    - [print](#print)
    - [string manipulation](#string-manipulation)
  - [dictionary methods](#dictionary-methods)
  - [Overview of commonly used Python Libraries](#overview-of-commonly-used-python-libraries)
    - [getpass](#getpass)
    - [os](#os)
    - [time](#time)
    - [random](#random)
## Overview commonly used subroutines
### print
```python
print('1','2','3', end='\n')
print('1','2','3', sep=' ')
# turn off the cursor in the terminal
print('\033[?25l', end="")
# color codes
print('\033[0;0m')
# 0   default
# 30  black 
# 31  red
# 32  green 
# 33  brown 
# 34  blue
# 35  purple
# 36  cyan
# 37  gray
```
### string manipulation
```python
## formatted strings
var1='Good day'
varé='Goodbye'
str = f'{var1} Hello World {var2}'
#old format 
str = "{var1} Hello World {var2}".format(var1=var1,var2=var2)

# alignment of variable values in string
print(f"Day {i:<2} of 30")  # aligns left 2 characters
print(f"Day {i:>2} of 30")  # aligns right 2 characters
print(f"Day {i:^35} of 30") # Use 35 characters and align center

## string manipulation methods
str.lower().upper()
str.capitalize().title()
str.strip()

# split string
splitStr = str.split()    #default is at whitespace
splitStr = str.split(',')

# string slicing
## str[begin index:index after end]
slicedStr = str[2:5] #cuts out character at index positions 2-3-4
slicedStr = str[0:1] #cuts out character at index positions 0
slicedStr = str[:1]  #cuts out character at index positions 0, leaving first index blank defaults to 0
slicedStr = str[0:]  #leaving ending index blank defaults to end of string
slicedStr = str[:]   #return every character from 0 to the end

slicedStr = str[0:5:2] #cuts out every second character between position 0 and 4
print(str[::3])        #print every third character in a string
print(str[:])          #print every third character in a string
print(str[::-1])       #print every third character in a string, starting from the end
```
## dictionary methods
```Python
# A standard for loop will only return the dictionary values. Use the items() method to access both name and value.
for val in myDictionary
  print(val)

for name,value in myDictionary.items():
  print(f"{name}:{value}")

```
## Overview of commonly used Python Libraries
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
```
### time 
Control timing
```python
import time
#pause execution x seconds
print('Hello')
time.sleep(1)
print('World')
```
### random 
Generate random numbers
```python
import random
num = random.randint(0,100)
```