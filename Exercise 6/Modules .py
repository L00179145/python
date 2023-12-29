############
Modules 
###################

#####
project.py
#######
import reusable
print("Running code from the project")
print(reusable.my_square(3))


#### I could use in more than one project is in reusable.py.
############
reusable.py
######
def my_square(a: int)->int:
    print("Running code from the module")
    return a*a
###############	
project.py
#########
import resuable
print("this is running code from project")
print(resuable.my_square(3))