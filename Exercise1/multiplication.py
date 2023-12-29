#multiplication table

digit1 = int(input("Enter a number for generating multiplication table: "))
digit2 = int(input("Enter the limit: "))
for x in range(1,digit2+1):
  print(str(digit1)+" * "+str(x)+" = "+str(digit1*x))