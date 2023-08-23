"""
1.Write the python code for display the numbers from starting number to endingnumber, we want to give conductions is divied by 2 and without Multiple of 4 number.

"""

number=int(input("Enter the Number : "))

for i in range (1,number):
    if i%2==0 and (not i%4==0):
        print(i)
