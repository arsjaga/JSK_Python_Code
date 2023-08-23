"""
2.Write a python code for Find the largest number in three number.

"""

a=int(input("Enter the A Value : "))
b=int(input("Enter the B value : "))
c=int(input("Enter the C value : "))

if a>b and a>c:
    print("A is Biggest Number ")
elif b>a and b>c:
    print("B is Biggest Number ")
elif c>a and c>b:
    print("C is Biggest Number ")
else:
    print("A,B and C are Equel ")


