def odd_even(number):
    if number % 2==0:
        print("Even Number")
    else:
        print("Odd Number")

def main():
    input_number=int(input("Enter the Number"))
    odd_even(input_number)

main()
