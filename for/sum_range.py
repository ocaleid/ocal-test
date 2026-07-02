num1 = int(input("please enter the first number: "))
num2 = int(input("please enter the second number: "))

sum = 0

for i in range(num1, num2 + 1):
    sum += i    

print(40* "*")
print(f"sum of number between {num1} and {num2} is : {sum}")