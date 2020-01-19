##
# My first Python program
#

print("Hello World!")

print("My lucky numbers are", 3*4+5, 5*6-1)

# print(1/0) #test zero division error

print("balance after one year: ", 10000*1.05)

print("balance after two years: ", 10000*1.05*1.05)

print("balance after fifteen years: ", 10000*1.05*1.05*1.05*1.05*1.05*1.05*1.05*1.05*1.05*1.05*1.05*1.05*1.05*1.05*1.05)

# Sum of first 10 positive integers
print(1+2+3+4+5+6+7+8+9+10," is the sum of the first 10 positive integers")

# My name in a box
print("_____")
print("|Tom|")
print("|---|")

# Table of friend's birthdays
print("_______________________")
print("| Friend  | Birthday   |")
print("|----------------------|")
print("| Alex    | 01/01/1990 |")
print("| Brenda  | 28/02/1970 |")
print("| Carl    | 16/10/1950 |")
print("|______________________|")

# Program to calculate the surface area to paint on a house
houseWidth = 6
houseLength = 6
houseHeight = 3

numberOfWindows = 5
windowLength = 1
windowHeight = 1
numberOfDoors = 2
doorLength = 2
doorHeight = 2

houseSurfaceArea = houseWidth * houseLength * houseHeight
windowSurfaceArea = (windowLength * windowHeight) * numberOfWindows
doorSurfaceArea = (doorLength * doorHeight) * numberOfDoors
roofSurfaceArea = houseWidth * houseLength

paintingArea = houseSurfaceArea - windowSurfaceArea - doorSurfaceArea - roofSurfaceArea

print("Surface area to paint: ", paintingArea)
