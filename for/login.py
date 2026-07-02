user= "eid"
pw= "123"

name_retry= True
pass_retry= True

for i in range(2):
    username= input("please enter your username: ") .lower()
    
    if username==user:
        
        for j in range(2):
            password= input("please enter your password: ")
            
            if password==pw:
                print("Welcome Eid")
                
                
            else:
                print("Wrong password")
                j = int(input("Do you want to try again? (1 for yes, 0 for no): "))
                
    else:
        print("Unknown user")
        i = int(input("Do you want to try again? (1 for yes, 0 for no): "))