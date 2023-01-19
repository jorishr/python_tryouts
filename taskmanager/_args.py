import argparse

msg = 'Hello, welcome to the Task Manager.'
parser = argparse.ArgumentParser(description=f'{msg}')
parser.add_argument('--debug', action='store_true', help='developer mode, see full error messages')
args = parser.parse_args()

debugMode = False
if args.debug:
    debugMode = True 
#print(debugMode)