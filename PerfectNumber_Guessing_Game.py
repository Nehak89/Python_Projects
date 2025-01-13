import random

t = 0 

g = int(input("Total Guesses: "))
low = int(input("Enter the lower range: "))
high = int(input("Enter the upper range: ")) 
x = random.randint(low, high)


while t < g:
    n = int(input(f"Enter an integer between {low} and {high}: "))
    if n < x:
        print("The number guessed is low")
        t += 1
    elif n > x:
        print("The number guessed is high")
        t += 1
    else:
        print("The number guessed is right")
        print("Total guesses taken:", t + 1)
        break
else:
    print("Ran out of tries! The correct number was:", x)
