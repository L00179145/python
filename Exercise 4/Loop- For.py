#################################
Loop- For
##################################
 
  
# Check even and odd numbers from the list
numbers_list = [11, 25, 30, 42, 55, 60, 73, 88, 91, 104]

for number in numbers_list:
    if number % 2 != 0:
        print('Odd numbers from the list:', number)

for number in numbers_list:
    if number % 2 == 0:
        print('Even numbers from the list:', number)

print('*******************************************************************************')

# Use scan.items to get output
scan = {"IIT Bombay": "Computer Science", "Delhi University": "Economics", "IISc Bangalore": "Biotechnology"}
for university, course in scan.items():
    print(f"Found top courses at {university}: The top course is {course}")

print('*******************************************************************************')

