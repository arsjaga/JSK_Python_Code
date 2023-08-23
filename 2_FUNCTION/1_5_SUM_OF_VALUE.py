def sum_of_value(n):
    sum=0
    for i in range (n):
        sum=sum+i
    return sum


def main():
    n=int(input("Enter the Number : "))
    output=sum_of_value(n)
    print(output)

main()
