def fibnocis(n):
    n1=0
    n2=1
    for i in range (0,n+1):
        n3=n1+n2
        print(n3)
        n1=n2
        n2=n3

def main():
    n=int(input("Enter the Number : "))
    fibnocis(n)
    
main()
