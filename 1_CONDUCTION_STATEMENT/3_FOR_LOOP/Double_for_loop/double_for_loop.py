def double_for_loop():
    n = int(input("Enter the Number : "))
    for i in range (0, n+1):
        for j in range (0, i+1):
            print(j, end=" ")
            j = j + 1
        print("\n")
        i = i + 1

if __name__ == "__main__":
    double_for_loop()
        
