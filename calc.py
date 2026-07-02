'''
while True:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    sum = 0

    while num1 <= num2:
        sum += num1 
        num1 += 1       

    print("The sum is:", sum)
    


    '''
    
'''for i in range(1, 11):
    print(i//2)'''
    
 
x = int(input("Enter a number: "))   
for i in range(10):
    result= i * x
    if result>=10:
        break
    print(result)