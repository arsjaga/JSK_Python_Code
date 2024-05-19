def factorial():
    """Factorial Number"""
    fact = 1
    INPUT = int(input("Enter the number"))
    for i in range (1,INPUT+1):
        fact = fact * i
        
    print(fact)  

if __name__ == "__main__":
    factorial()

    
