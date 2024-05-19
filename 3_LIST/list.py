#Prog 1:

ages = [34, 35, 36]
print(ages)
print(ages[0], ages[1], ages[2])

for i in range (len(ages)):
    print(ages[i])

# a list containing strings and numbers
student = ['Jack', 32, 'Computer Science']
print(student)
print(student[0], student[1], student[2])


# an empty list
empty_list = []
print(empty_list)
# convert to list
x = "axz"
result = list(x)
print(result)  # ['a', 'x', 'z']


# Negative indexing
languages = ['Python', 'Swift', 'C++']
# access item at index 0
print(languages[-1])   # C++
# access item at index 2
print(languages[-3])   # Python



# Slicing of a List in Python 
my_list = [11,2,3,4,5]
# items from index 2 to index 4
print(my_list[2:5])
# items from index 5 to end
print(my_list[5:])
# items beginning to end
print(my_list[:])


# Add Elements to a Python List

# append()
fruits = ['apple', 'banana', 'orange']
print('Original List:', fruits)
# using append method 
fruits.append('cherry')
print('Updated List:', fruits)


# insert()
fruits = ['apple', 'banana', 'orange']
print("Original List:", fruits) 
# insert 'cherry' at index 2
fruits.insert(2, 'cherry')
print("Updated List:", fruits)

#  extend()
numbers = [1, 3, 5]
print('Numbers:', numbers)
even_numbers  = [2, 4, 6]
# adding elements of one list to another
numbers.extend(even_numbers)
print('Updated Numbers:', numbers) 

# Change List Items
colors = ['Red', 'Black', 'Green']
print('Original List:', colors)
# changing the third item to 'Blue'
colors[2] = 'Blue'
print('Updated List:', colors)

# Remove an Item From a List
numbers = [2,4,7,9]
# remove 4 from the list
numbers.remove(4)
print(numbers) 
# Output: [2, 7, 9]

# Remove One or More Elements of a List 
names = ['John', 'Eva', 'Laura', 'Nick', 'Jack']
# deleting the second item
del names[1]
print(names)
# deleting items from index 1 to index 3 
del names[1: 4]
print(names) # Error! List doesn't exist.


# names = ['John', 'Eva', 'Laura', 'Nick']
# # deleting the entire list
# del names
# print(names)

# Python List Length
cars = ['BMW', 'Mercedes', 'Tesla']
print('Total Elements: ', len(cars))  
# Output: Total Elements:  3

# Iterating Through a List
fruits = ['apple', 'banana', 'orange']
# iterate through the list
for fruit in fruits:
    print(fruit)

# List Comprehension in Python 
# create a list with square values
numbers = [n**2 for n in range(1, 6)]
print(numbers)  
# Output: [1, 4, 9, 16, 25]

# Check if an Item Exists in the Python List 
fruits = ['apple', 'cherry', 'banana']
print('orange' in fruits)    # False
print('cherry' in fruits)    # True
