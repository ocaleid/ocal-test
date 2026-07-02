counter = 0

for i in range(1, 31):
    if i % 2 == 0:
        print(i)
        counter += 1

print("Total even numbers: ", counter)