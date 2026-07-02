def fun_list(list, list_name):
    list_len=int(input(f"Enter the number of items you want to add to {list_name} list: "))
    for i in range(list_len):
        list[i]=(input(f"Enter item {i+1} for {list_name}: "))
    
    print(f"{list_name}: {list}")


product=[]
numbers=[]
names=[]

fun_list(product, "Product")
fun_list(numbers, "Numbers")
fun_list(names, "Names")