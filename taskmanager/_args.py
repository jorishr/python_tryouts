import argparse

msg = 'Hello, welcome to the Task Manager.'
parser = argparse.ArgumentParser(description=f'{msg}',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--debug', action='store_true', help='developer mode, see full error messages')
arg = parser.parse_args()
config = vars(arg)

debugMode = bool(config['debug'])
#print(debugMode)