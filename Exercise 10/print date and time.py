
############

code to print date and time
#################################
from datetime import datetime as d_tyy

# Defining variable to print date 
a = d_tyy.now()
print(a)

# Converting datetime to UNIX timestamp
unix_time = a.timestamp()
print(unix_time)
