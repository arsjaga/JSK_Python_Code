def for_loop_forward(n):
    print("Print the Number From 0 to N")
    for i in range (0, n+1):
        print(i)

def for_loop_reverse(n):
    print("Print the Number From N to 0")
    for i in range (n, 0-1, -1):
        print(i)

def while_loop_forward(n):
    print("Print the Number From 0 to N\n")
    i = 0
    while(i < n):
        print(i)
        i += 1

def while_loop_reverse(n):
    print("Print the Number From N to 0\n")
    i = n
    while(i > 0):
        print(i)
        i -= 1

def sum_of_value(n):
    sum = 0
    for i in range (0, n+1):
        sum = sum + i
    print("sum = ",sum)

def factorial_number(n):
    fact = 1
    i = 1
    while(i < n):
        fact = fact * i
        i += 1
    print("Factorial Number  = ", fact)

def prime_number(n):
    count = 0 
    for i in range (1, n+1):
        if (n % i == 0):
            count += 1
    
    if(count == 2):
        print("This is Prime Number")
    else:
        print("This is not Prime Number")

def prime_upto_100():
    for n in range (1, 101):
        count = 0
        for i in range (1, n+1):
            if(n % i == 0):
                count += 1
        if (count == 2):
            print(n)



for_loop_forward(10)
for_loop_reverse(5)
while_loop_forward(10)
while_loop_reverse(5)
sum_of_value(5)
factorial_number(5)
prime_number(7)
prime_upto_100()