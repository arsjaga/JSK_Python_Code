def prime_number():
    for n in range (1, 101):
        COUNT = 0
        for i in range(1, n+1):
            if n%i == 0:
                COUNT = COUNT+1
        if COUNT == 2:
            print(n)

if __name__ == '__main__':
    prime_number()
