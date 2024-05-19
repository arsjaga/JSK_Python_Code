def prime_number(n):
    COUNT = 0
    for i in range(1, n+1):
        if n%i == 0:
            COUNT = COUNT+1
    
    if COUNT == 2:
        print("Prime Number")
    else:
        print("Not Prime Number")


if __name__ == '__main__':
    INPUT_NUMBER = int(input("Enter the Number"))
    prime_number(INPUT_NUMBER)
