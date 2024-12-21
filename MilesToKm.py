#!/user/bin/env python3

# Matthew Taylor
# Cuyamaca College CS-119
# Lab 1, exercise 3, convert miles to kilometers

# declare variables
miles = 0
kilometers = 0
conversion = 0.62

# input - get miles from user
miles = float( input('Enter miles: ') )

# process - convert miles from user to km (1 mile = 0.62 km)
kilometers = miles / conversion

# output
print( str(kilometers) + ' kilometers' )
