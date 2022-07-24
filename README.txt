***Object Model for Project Management Application***

#code developed with Python 3.10.4 version

#Objects involved

Project
Task
User -> Project Owner
Resource -> Users assigned to the Project

i) Project can contain multiple tasks 
ii) Each task can be peformed by users utilising the Resources adhering to schedule
iii) Task has an start and end date and its predecessor and successor
iv) User has roles such as admin(to create a project), Common user (resource for the tasks)