'''def print():
    name = ["Ahmed", "Eid"]
    name.append("Sara")
    print(name)
'''
def user_in(list):
    while True:
        user_input= input("Enter username: ")
        if user_input== "0": 
            break
        list.append(user_input)
        
def update(list):
    index= int(input("Enter the number of username you want to update: "))
    list[index]= input("Enter the updated username: ")
        
        
def main():
    list=[]
    user_in(list)
    print(list)
    update(list)
    print(list)
    
main()
    