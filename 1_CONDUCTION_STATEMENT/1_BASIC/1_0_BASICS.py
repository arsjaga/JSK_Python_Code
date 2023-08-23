"""
1.Write a Python function to check if a number is even or odd. The function should take an integer as input and return "Even" if the number is even, and "Odd" if the number is odd.
"""

# function to check the odd or even 
def check_odd_or_even(input_number):

	if input_number % 2 == 0:
		return "Even"
	else:
		return "Odd"


if __name__ == '__main__':
	# variabel to store input number
	input_num = input("Enter the input as whole numbers: ")

	# function call if number is digit and print the status,otherwise exit
	print("The number is",check_odd_or_even(int(input_num))) if input_num.isdigit() else print("Is not whole number ")

