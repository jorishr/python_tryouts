## Virtual Environment
Virtualenv is a tool to create isolated Python environments.
```bash
sudo apt-get install python3-pip
sudo pip install virtualenv

# create a folder to store the environments for each app
mkdir ~/.virtualenvs

# in that folder create the new env
virtualenv myNewEnvironment
virtualenv -p usr/bin/python2.8 myNewEnvironment # specify a python version

# activate
source ~/.virtualenvs/myNewEnvironment/bin/activate

# go back to global environment
deactivate

which python # shows the path to the virtual environment
pip list # see the packages

# output required packages for your project into txt file 
pip freeze --local > requirements.txt
pip install -r requirements.txt
```
