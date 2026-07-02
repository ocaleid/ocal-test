user= {"name": "Eid", "age": 24, "job": "Engineer"}


print(user["name"])
print(user["age"])

if "job" in user:
    print(user["job"])
else:
    print("Job not found")
    
print(user)

for key in user:
    print(key, user[key])
    
    zhraa = {
        "1": [0, 1, 2, 3],
        "2": [0, 1, 2],
        "3": [0,1, 2, 3, 4],
        "4": [0, 1, 2]
    }