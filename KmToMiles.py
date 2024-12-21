#!/user/bin/env python3

# Matthew Taylor
# Cuyamaca College CS-119
# Lab 1, exercise 2, convert kilometers to miles

# declare variables
kilometers = 0
miles = 0
conversion = 0.62

# input - retrieve km from user
kilometers = float( input('Enter kilometers: ') )

# process - convert users km to miles (1 km = 0.62 miles)
miles = kilometers * conversion

#output
print( str(miles) + ' miles' )
