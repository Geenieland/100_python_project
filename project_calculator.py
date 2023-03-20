#Final Calculator

#Add
def add(n1, n2):
  return n1 + n2
#Subtract
def subtract(n1, n2):
  return n1 - n2
#Multiple
def multiple(n1, n2):
  return n1 * n2
#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiple,
  "/": divide  
}

def calculator():
  
  num1 = int(input("What is your first number? "))
  for number in operations:
    print(number)
  
  answer_result = True
  
  while answer_result:
    
    operation_symbol = input("Pick an operation: ")
    num2 = int(input("What is your second number? "))
    first_calculation_function = operations[operation_symbol]
    answer = first_calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer} ")
    
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ").lower() == "y":
      num1 = answer
      
    else:
      answer_result = False
      calculator()


calculator()
