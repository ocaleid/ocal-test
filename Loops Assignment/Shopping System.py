item_count=0
item_price=0
max_price=0
min_price=0
total_price=0
avg_price=0

while True:
    item_price = float(input("Enter item price or 0 to finish: "))
    if item_price == 0:
        break
    item_count += 1
    total_price += item_price
    if item_price > max_price:
        max_price = item_price
    if item_price < min_price or min_price == 0:
        min_price = item_price
 
if item_count == 0 and item_price == 0:
    print("No items were added.")
else:
    if item_count > 0:           
        avg_price= total_price / item_count 

    print("Number of items: ", item_count)
    print("Total price: ", total_price)
    print("Average item price: ", avg_price)
    print("Most expensive item: ", max_price)
    print("Cheapest item: ", min_price)