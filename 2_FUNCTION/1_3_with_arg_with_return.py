# With Argument and With Return Values


def fun_with_arg_with_return(a,b):
    sum=a+b
    return sum


def main():

    a=int(input("Enter the A value"))
    b=int(input("Enter the B value"))
    c=fun_with_arg_with_return(a,b)
    print("Result=",c)

main()
