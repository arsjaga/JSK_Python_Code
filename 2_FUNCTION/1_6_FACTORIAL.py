def fact_number(n):
    fact=1
    for i in range (1,n+1):
        fact=fact*i
    return fact

def main():
    n=int(input("Enter the Number : "))
    output=fact_number(n)
    print(output)

main()
