#1e - debugging
#coding exercise: shopping

meatPrice = 4.00
meatTax = 0.03 * meatPrice
milkPrice = 2.00
milkTax = 0.03 * milkPrice
print(meatTax + meatPrice + milkTax + milkPrice)

# you can of course also do this less verbosely like so

total = 4.00 + 2.00	# add milk and meat prices
tax = total * 0.03 	# get the tax 
print(total + tax)