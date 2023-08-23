# Without Argument and With return Values

def fun_without_arg_with_return():
    a=int(input("Enter the A value : "))
    b=int(input("Enter the B value : "))
    c=a+b
    return c


def main():
    sum=fun_without_arg_with_return()
    print("Result=",sum)

main()
