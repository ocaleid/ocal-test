num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

operation=input("Enter the operation (+, -, *, /): ")

def op_sum(num1, num2):
    return num1 + num2

def op_diff(num1, num2):
    return num1 - num2

def op_prod(num1, num2):
    return num1 * num2

def op_div(num1, num2):
    return num1 / num2

if operation == "+":
    result = op_sum(num1, num2)
elif operation == "-":
    result = op_diff(num1, num2)
elif operation == "*":
    result = op_prod(num1, num2)
elif operation == "/":
    result = op_div(num1, num2)
else:
    result = "Wrong operation"
    
print(f"The result of {num1} {operation} {num2} is: {result}")