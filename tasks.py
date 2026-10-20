import json #Allows data to be stored and retrieved JSON format

def save_tasks():
    with open("tasks.json", "w") as file: #Opens file for writing and creates it if it does not exist. with closes file after operation is completed
        json.dump(taskList,file,indent=4) #Converts taskList into JSON format and writes it to a file
def load_tasks():
    global taskList #Ensures taskList is global
    try:
        with open("tasks.json","r") as file: #Opens file for reading
            taskList = json.load(file) #Loads file and assigns it to taskList
    except FileNotFoundError:
        taskList=[] #Task list is empty if saved one cannot be found

def add_task(userTask):
    userTask=userTask.strip()
    if userTask=="":
        return False
    else:
        taskList.append({"name":userTask, "completed":False}) #Dictionary used to also store the completion status
        save_tasks()
        return True
    
def complete_task(index):
    if len(taskList)>0:
        taskList[index]["completed"]=True
        return True
    else:
        return False
        
def delete_task(index):
    if len(taskList)>0 and (index>=0 and index<=(len(taskList)-1)):
        taskList.pop(index)
        save_tasks()
        return True
    else:
        return False
        
#Program starts here
load_tasks()



