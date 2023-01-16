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

    def getDeadline(self):
        return self.deadline

    def getPriority(self):
        return self.priority
    
    def getAll(self):
        return [self.name,self.deadline,self.priority]

    def setName(self, name):
        self.name = name   
    
    def setDeadline(self, deadline):
        self.deadline = deadline

    def setPriority(self, priority):
        self.priority = priority

task1 = Task('work', 'today', 'low')
#print(task1.getName())
#print(task1.getPriority())
#task1.setPriority('high')
#print(task1.getAll())