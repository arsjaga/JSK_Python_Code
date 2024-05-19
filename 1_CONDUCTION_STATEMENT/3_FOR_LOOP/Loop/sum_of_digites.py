def sum_of_digites():
    """Sum of digites Number"""
    sum = 0
    INPUT = int(input("Enter the number"))
    for i in range (0,INPUT+1):
        sum = sum + i
        
    print(sum)  

if __name__ == "__main__":
    sum_of_digites()

    
