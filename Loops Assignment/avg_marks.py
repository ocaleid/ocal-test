marks_count = int(input("How many marks do you want to enter?  "))
total_marks = 0

print("\n *****************")
for i in range(marks_count):
    mark = int(input(f"Enter mark {i+1}: "))
    total_marks += mark

print("\n *****************")
average_mark = total_marks / marks_count
print(f"\nAverage:: {average_mark}")