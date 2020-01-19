##
# This program computes the volume (in litres) of a six-pack of soda
# cans, the total volume of a six-pack and a two-litre bottle and price.
#

# Litres in a 12-ounce can and a two-litre bottle.
CAN_VOLUME = 0.355
BOTTLE_VOLUME = 2.0

# Number of cans per pack.
cansPerPack = 6

# Calculate total volume in the cans.
totalVolume = cansPerPack * CAN_VOLUME
print("A six-pack of 12-ounce cans contains", totalVolume, "litres.")

# Calculate total volume in the cans and a 2-litre bottle.
totalVolume = totalVolume + BOTTLE_VOLUME
print("A six-pack and a two-litre bottle contain", totalVolume, "litres.")

unitPrice = 2
quantity = 2

print(unitPrice * quantity)

