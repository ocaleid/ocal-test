while True:
    print("**********************************************************************")
    num1=float(input("enter the first number: "))
    num2=float(input("enter the second number: "))
    operation =input("What is the operation do you want? (/,*,+,-) enter 0 to exit: ")
    result=0    
    print("**********************************************************************")
        
    if operation=="/":
        result=num1/num2
        print(f"{num1}/{num2}={result}")
    
    elif operation=="*":
        result=num1*num2
        print(f"{num1}*{num2}={result}")
    
    elif operation=="+":
        result=num1+num2
        print(f"{num1}+{num2}={result}")
    
    elif operation=="-":
        result=num1-num2
        print(f"{num1}-{num2}={result}")
    
    elif operation=="0":
        break
        
    else:
        print("wrong operation please try again")