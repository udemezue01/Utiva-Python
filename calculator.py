

# While loops

# if , else statement

# artithmetic operators 


while True:

	print("This is a python calculator")

	print ("Type add Keyword to make use of the addition functionality.")

	print ("Type minus  Keyword to make use of the Subtration functionality.")

	print ("Type divide Keyword to make use of the Division functionality.")

	print ("Type multiply Keyword to make use of the Multiplicaton functionality.")

	user_input  = input(":")

	if user_input == "add":

		num1  = float(input(" Enter the first number"))

		num2  = float(input(" Enter the second number"))

		result = num1 + num2

		print(f'The sum of {num1} and {num2} is {result} ')

	elif user_input =="minus":

		num1  =  float(input("Enter the first number"))

		num2  =  float (input("Enter the second number"))

		result = num1 - num2

		print(f'The Subtration of {num1} and {num2} is {result} ')

