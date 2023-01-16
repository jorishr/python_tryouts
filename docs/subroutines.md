## Overview commonly used subroutines
- [Overview commonly used subroutines](#overview-commonly-used-subroutines)
  - [print](#print)
  - [string manipulation](#string-manipulation)
  - [list methods](#list-methods)
  - [dictionary methods](#dictionary-methods)
  - [read and write to files](#read-and-write-to-files)
  - [error handling](#error-handling)

### print
```python
# by default the print statement ends with a new line.
print('1','2','3', end='') # statement will end on same line
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
var2='Goodbye'
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
str.find('a') #returns index position or -1 if not found
str.find('word')

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
print(str[::-1])       #print every character in a string, starting from the end

# hash a string with built-in method
password = '123456'
salt = random.randomint(10000,99999999)
newPassword = f'{password}{salt}'
storedPwInDB = hash(newPassword)

# replace a text string within a string
str = 'Hello world'
print(str.replace('world','you'))
name = 'jr'
str = f'Hello, {name}'
str.replace(f'{name}','sps')
print(str)
```
### list methods
```python
# get access to index in for loop
dataList = ['first', 'second']
for i,val in enumerate(dataList):
  num = i + 1
  print(f'{num}. val')
# prints: 
# 1. first 
# 2. second 
```
### dictionary methods
```Python
# A standard for loop will only return the dictionary values. Use the items() method to access both name and value.
for val in myDictionary
  print(val)

for key,value in myDictionary.items():
  print(f"{key}:{value}")

```
### read and write to files
```python
# This is a three step process: open a file, read or write to it, and store/close the file.
f = open('filename.extension', 'r/w/a/a+')
content = 'string'
f.write(f'{content}\n')

content = [] #cast lists or dictionaries into a string format
f.write(str(content))

#write an empty file
f.open('path-filename', 'w')
f.close()

content = f.read() #reads entire file
content = f.readline() #reads one line, use while loop to get to the end

while True:
  contents = f.readline().strip()
  if contents == '':
    break
  print(contents)
f.close()

# write binary data (images, for example) 
image = requests.get('api/endpoint')
f.open(fileName, 'wb')
f.write(image.content)
f.close()

# evaluate a string that contains valid code: example, a list or dictionary.
data = eval(f.read())
```
### error handling
```python
try:
  #code
except Exception as e:
  print('User friendly error message')
  if debugMode:
    #add a debug variable at the start of the program
    print(e)
  # do something useful to the user
```