numbers=[1,2,3,4,5]

print("List the numbers:",numbers)

number_add=[6,7]

numbers.extend(number_add)

print("List all the numbers in list:",numbers)

string="India"

numbers.extend(string)

print("List include string in list:",numbers)

numbers.extend([5,5,5,5])

print("List include list:",numbers)
