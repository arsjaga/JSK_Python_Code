"""
0
0       1
0       1       2
0       1       2       3
0       1       2       3       4
0       1       2       3       4       5
"""

def triangle_pattern_1(n):
    print("Print the Stars")
    for i in range(0, n+1):
        for j in range(0, i + 1):
            print(j, end='\t')
        print()


"""
*
*       *
*       *       *
*       *       *       *
*       *       *       *       *
*       *       *       *       *       *
"""
def triangle_pattern_2(n):
    print("Print the Stars in reverse")
    for i in range (n, 0, -1):
        for j in range (i, 0, -1):
            print(j, end = '\t')
        print()




"""
*
*       *
*       *       *
*       *       *       *
*       *       *       *       *
*       *       *       *       *       *
"""
def triangle_pattern_3(n):
    print("Print the Stars in reverse")
    for i in range (n, 0, -1):
        for j in range (i, 0, -1):
            print('*', end = '\t')
        print()




"""
*       *       *       *       *
*       *       *       *
*       *       *
*       *
*
"""
def triangle_pattern_4(n):
    print("Print the Stars")
    for i in range(0, n+1):
        for j in range(0, i):
            print('*', end='\t')
        print()



triangle_pattern_2(5)

