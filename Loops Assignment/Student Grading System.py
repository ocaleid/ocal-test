mark_total = 0
passed=0
failed=0
top_student = ""
highest_average = 0


st_number = int(input("How many students do you want to enter? "))

for i in range(st_number):
    print("*************************")
    name = input("\nEnter student name: ")
    mk_number = int(input(f"How many marks for {name}? "))
    i+= 1
    mark_total = 0
    
    for j in range(mk_number):
        mark = float(input(f"Enter mark {j+1} for {name}: "))
        mark_total = mark_total + mark
        j += 1
    
    average_mark = mark_total / mk_number
    
    if average_mark > highest_average:
        highest_average = average_mark
        top_student = name
        
    print(f"{name}'s average mark is: {average_mark}")
    
    if average_mark >= 50:
        print("Result: Passed :)\n")
        passed += 1
    else:
        print("Result: Failed :(\n")
        failed += 1

print("*************************\nSummary:")
print(f"Total students: {st_number}")
print(f"Passed students: {passed}")
print(f"Failed students: {failed}")
print(f"Highest average: {highest_average}")
print(f"Top student: {top_student}")
