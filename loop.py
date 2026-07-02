user= "eid"
pw= "123"

name_retry= True
pass_retry= True

while name_retry:
    username= input("please enter your username: ") .lower()
    
    if username==user:
        name_retry= False
        
        while pass_retry:
            password= input("please enter your password: ")

            
            if password==pw:
                print("Welcome Eid")
                pass_retry= False
                
            else:
                print("Wrong password")
                
    else:
        print("Unknown user")