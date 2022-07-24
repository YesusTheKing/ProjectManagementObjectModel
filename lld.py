from abc import ABC


#Iuser abstract class for all the types of owner

class IUser(ABC):
    pass

class IProject(ABC):
    pass

class ITask(ABC):
    pass

class Admin(IUser):
    pass

class Resource(IUser):
    pass

class Project(IProject):
    pass

class Task(ITask):
    pass

class Application(object):
    pass
