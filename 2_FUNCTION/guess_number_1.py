import random 
def computer_guess():
    return random.randrange(100)

def user_guess():
    while True:
        user_number = int(input("Enter the Number : "))
        # if len(user_number) > 2:
        #     print("You enter the wrong number")
        #     continue
        # break
        return user_number

def check_guess(cmp_number, user_number):
    if cmp_number > user_number:
        print("You entered smaller number")
    elif cmp_number < user_number:
        print("You entered greater number")
    elif cmp_number == user_number:
        print("You entered the Guess number")
        return True
    return False    

if __name__ == "__main__":
    cmp_number = computer_guess()
    chance = 7
    while chance > 0:
        user_number = user_guess()
        guess = check_guess(cmp_number, user_number)
        if guess == 1:
            break
        chance -= 1
    if(chance == 0):
        print("You lose the game")
