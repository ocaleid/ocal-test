secret_number = 7

while True:
    guess = int(input("Guess the number: "))
    
    if guess < secret_number:
        if secret_number - guess <= 3:
            print("Low, but you're close! :)")
        else:
            print("Too low! :(")
    elif guess > secret_number:
        if guess - secret_number <= 3:
            print("High, but you're close! :)")
        else:
            print("Too high! :(")
    else:
        print("Correct! :)")
        break