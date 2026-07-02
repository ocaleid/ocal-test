print("************************************")
username= input("please enter your username: ")

user1="Eid"
pass1=123
role1="Moderator"

user2="Shoman"
pass2=111
role2="Admin"

user3="Ahmed"
pass3=321
role3="User"


if username==user1 or username==user2 or username==user3:
    password= int(input("please enter your password: "))
    print("************************************\n")   
     
    if (username==user1 and password==pass1) or (username==user2 and password==pass2) or (username==user3 and password==pass3):
        role=input("please enter your role (Admin, Moderator, User) :")
        print("\n************************************\n")
        
        if (username==user1 and role=="Moderator")  or (username==user2 and role=="Admin") or (username==user3 and role=="User"):
         print("Welcome", role)
        
        else:
            print("Unknown role")
        
    else:
        print("Wrong password")
        
else:
    print("************************************\n")
    print("User not found")
    
print("\n************************************")