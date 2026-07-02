class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")
        
    def login(self):
        print(f"{self.name} is logged in.")
        
    def logout(self):
        print(f"{self.name} is logged out.")
        
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age
        
user1 = User("Eid", 24)
user2 = User("Shoman", 30)

print(user1.get_name())
print(user2.get_age())
print(user1.name)
