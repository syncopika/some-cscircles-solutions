# coding exercise: payment calculator

a = balance
b = .021 * a	# calculate the balance times the percentage given first 
c = max(min(10, a), b)    # use min to choose the smaller between 10 and a. then use that result to compare with b. 