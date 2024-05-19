import random 
rand_number = random.randint(0,99)
print(rand_number)
chances = 7

while chances > 0 :
    user_input = int(input("Enter the Number"))
    if user_input == rand_number:
        print("Your guess number is = ", rand_number)
        break
    elif user_input > rand_number :
        print("your guess number is greater")
    elif user_input < rand_number :
        print("Your guess number is lesser ")
    chances = chances - 1
if chances == 0 :
    print("Try Again")