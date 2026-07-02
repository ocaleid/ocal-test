while True:
    i= int(input("Enter your number: "))
    a=0
    b=1
    j=0

    print(a)
    print(b)
    i-=2

    while i!=0:
        j=a+b 
        a=b 
        print(j)
        b=j
        i-=1