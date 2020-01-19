##
# This program converts the dimensions of a letter from inches to millimeters.
#

# Letter dimensions
letterWidthInches = 8.5
letterLengthInches = 11

MILLIMETERS_PER_INCH = 25.4

# Dimensions converted from inches to millimeters
print("The letter size ", letterWidthInches, " inch x ", letterLengthInches, " inch converted into millimeters is ",
      letterWidthInches * MILLIMETERS_PER_INCH, "mm x ", letterLengthInches * MILLIMETERS_PER_INCH, "mm.")

purchase = 19.93
payment = 20.00
change = payment - purchase
print("Change £",round(change, 2))

##
# This program prints the first and last three characters of a string.

s = "Brazil"

print(s[:3],"...",s[3:])

s = "test"

print(s[1])
print(s+"2")
