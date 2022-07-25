from abc import ABC, abstractmethod,ABCMeta
import datetime as dt

class User:
    def __init__(self):
        #instance attributes
        self._user_id = None
        self.username = None
        self.email_address = None
        self.status = None
    
    def perform_task(self,task):
        pass
    def __str__(self):
        pass

class Resource:
    def __init__(self):
        #instance attributes
        self._resource_id = None
        self.resource_name = None
    
    def utilize(self):
        pass
    def __str__(self):
        pass

class Schedule:
    def __init__(self):
        self.startdate = None
        self.enddate = None
        self.duration = None
    
    def update_duration(self,startdate,enddate):
        pass
    def __str__(self):
        pass

class Task:
    def __init__(self):
        #instance attributes
        self._task_id:int = None
        self.task_name:str = None
        self.Resource:Resource = None
        self.schedule: Schedule = None
        self.predecessor:Task = None
        self.successor:Task = None
        self.is_completed:bool = None
    
    def operation(self):
        pass
    def update_resource(self,res:Resource):
        pass
    def update_taskname(self,name:str):
        pass
    def update_schedule(self,startdate,enddate):
        pass
    def update_predessor(self,task):
        pass
    def update_successor(self,task):
        pass
    def __str__(self):
        pass

class Project:
    
    def __init__(self,*args):
        self.tasks: list[Task] = []
        self.owner: User = None
        self.__pid: int = None
        self.projectname:str = None
    
    def update_projectname(self) -> None:
        pass
    
    def update_owner(self) -> None:
        pass
    
    #add task to project
    def add_task(self,task:ITask) -> None:
        pass
    
    #create task and add to the project
    def create_task(self,**kwargs) -> None:
        pass

    def delete_task(self,task) -> None:
        pass

    def do_task(self,task) -> bool:
        pass
    
    #return all the tasks of project
    def return_tasks(self) -> list[ITask]:
        pass
    
    #function to check whether the project can completed within target date
    def can_complete(self,target_date) -> bool:
        pass
    
    def __str__(self):
        pass


class Application(object):
    
    #initialize the application object with empty projects and users
    def __init__(self):
        self.projects :list[Project] = None
        self.users:list[User] = None
        self.resource:list[Resource] = None
    
    def add_project(self,project:IProject) -> None:
        pass
    
    def add_user(self,user:IUser) -> None:
        pass
    
    def add_resource(self,user:Resource) -> None:
        pass

    def can_complete_project(self,project:Project) -> bool:
        pass

    def __str__(self):
        pass
