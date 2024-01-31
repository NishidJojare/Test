from task_package.create_task import create_task 
from task_package.edit_task import edit_task 
from task_package.categorize_task import categorize_task 

# create a task
task1=create_task("Complete Your Assignment","Finish TASK MANAGEMENT SYSTEM")

# display the task
print("Task 1 : ",task1)

# edit the task
edit_task(task1,new_title="Updated Assignment",new_description="Review and Submit to Rashmi Mam")

# display the updated task
print("Updated Task 1 : ",task1)

# Categorize Task
categorize_task(task1,"Zappkode Academy")

# display the categorized task
print("Categorized Task 1 : ",task1)



'''
output : 

Task 1 :  Complete Your Assignment - Finish TASK MANAGEMENT SYSTEM (Category : None)
Updated Task 1 :  Updated Assignment - Review and Submit to Rashmi Mam (Category : None)
Categorized Task 1 :  Updated Assignment - Review and Submit to Rashmi Mam (Category : Zappkode Academy)

'''