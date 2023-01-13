class Task:
    name = None
    deadline = None
    priority = None

    def __init__(self, name, deadline, priority):
        self.name = name
        self.deadline = deadline
        self.priority = priority
    
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPriority(self):
        return self.priority
    
    def setPriority(self, priority):
        self.priority = priority
    
    def getDeadline(self):
        return self.deadline
    
    def setDeadline(self, deadline):
        self.deadline = deadline

task1 = Task('work', 'today', 'low')
#print(task1.getName())
#print(task1.getPriority())
#task1.setPriority('high')
#print(task1.getPriority())