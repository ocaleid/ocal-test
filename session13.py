data = [
    ["morning", "evening"],
    {"weather": {"today": "sunny", "tomorrow": "rainy"}},
    ["hot", "cold"],
]

def format_data(data):
    for i in range(len(data)):
        if type(data[i]) == list:
            for j in range(len(data[i])):
                print(data[i][j])
                
        elif type(data[i]) == dict:
            for key, value in data[i].items():
                print(key)
                format_data([value])
            


format_data(data)