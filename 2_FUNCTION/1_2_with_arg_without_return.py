# With Argument and Without Return Values

def fun_without_return(number):
    if number>90:
        print("A grade")

    elif number>80 and number<=90:
        print("B grade")

    elif number>70 and number<=80:
        print("C grade")

    elif number>60 and number<=70:
        print("D grade")

    elif number>50 and number<=60:
        print('E grade')

    else:
        print("Fail")

def main():
    print("Enter the A and B values:");
    a=int(input())
    b=int(input())
    c=a+b
    fun_without_return(c)

main()
