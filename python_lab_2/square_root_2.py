##
# This program calculates the square root of 2, originating from ITP LAB week 2slides.
#

# Initialize x
x=1.0
print("x*x:", x*x)

# First iteration
delta = (1/x)-x/2
x = x+delta
print("x*x:" , x*x)

# Second iteration
delta = (1/x)-x/2
x = x+delta
print("x*x:", x*x)

# Third iteration
delta = (1/x)-x/2
x = x+delta
print("x*x:", x*x)

# Fourth iteration
delta = (1/x)-x/2
x = x+delta
print("x*x:", x*x)
