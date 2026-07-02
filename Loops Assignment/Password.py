password = "python123"

i=3

while i > 0:
    user_pass = input("Please enter your password:")
    
    if user_pass == password:
        print("\nAccess granted\n")
        break
    else:
        i -= 1
        print("\nplease try again\n")
        
'''if i == 0:'''
    print("\nAccount locked\n")