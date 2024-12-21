#!/user/bin/env python3

# Matthew Taylor
# Cuyamaca College CS-119
# Lab 1, exercise 1, multiply 2 numbers

# declare variables
number1 = 0
number2 = 0
product = 0

# input - get input value from the user and convert to an integer
number1 = int( input("Enter first number: ") )
number2 = int( input("Enter second number: ") )

# process - note we use the * as a multiplication operator
product = number1 * number2

# output - The + operator used for concatentation. str() converts number to string
print( "The product is " + str(product) )
