def calculate_total(price, quantity):
    total = price * quantity
    total_with_tax = total + (total * 0.15)
    return total_with_tax

total_price = 0
i= int(input("Enter the number of items: "))
for i in range(i):
    price = float(input(f"Enter the price of item {i+1}: "))
    quantity = int(input(f"Enter the quantity of item {i+1}: "))
    total_price += calculate_total(price, quantity)
    
print(f"The total price with tax is:{total_price}")