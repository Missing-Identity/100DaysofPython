#Addition
def add(n1, n2):
  return n1+n2
#Subtraction
def subtraction(n1, n2):
  return n1-n2
#Multiplication
def multiplication(n1, n2):
  return n1*n2
#Division
def division(n1, n2):
  return n1/n2
#Remainder
def remainder(n1, n2):
  return n1%n2
#Operations dictionary
operations = {
  "+": add, 
  "-": subtraction, 
  "*": multiplication, 
  "/": division, 
  "%": remainder
  }

#Importing ASCII Art
import calc_art
print(calc_art.logo)

#User Input
number_1 = float(input("Enter the first number: \n"))
for key in operations:#Printing Operation symbols
  print(key)
operation_symbol = input("Pick an operation from above: \n")
number_2 = float(input("Enter the second number: \n"))

#Output function for the user's chosen operation
def output(operation, num1, num2):
  result = operations[operation](num1, num2)
  return round(float(result),4)

#Final Output
result = output(operation_symbol, number_1, number_2)
print(f"{number_1} {operation_symbol} {number_2} = {result}")

#User Continuation Loop
condition = False
calc_loop = True
while calc_loop == True:
  while condition == False:
    another_operation = input(f"Do you want to continue doing another operation using the previous result: {result}? Y for Yes and N for No: \n").lower()
    if another_operation == 'y' or another_operation == 'n':
      condition = True
    else:
      condition = False
      print("Not a valid input! Please type either 'Y' or 'N'! \n")
  if another_operation == "n":
    calc_loop  = False
    print(f"Final answer of your entire operation is: {result}")
  else:
    condition = False
    calc_loop = True
    previous_result = result
    operation_symbol = input("Enter the operation you want to do: \n")
    number_3 = int(input("Enter the next number you want to operate with: \n"))
    result = output(operation_symbol, result, number_3)
    print(f"{previous_result} {operation_symbol} {number_3} = {result}\n")