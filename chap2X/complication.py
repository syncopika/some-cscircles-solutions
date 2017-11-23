# coding exercise: complication

# when you have a smaller and bigger number, the smaller number's negative will always be bigger than the larger one's!
# don't forget that writing out examples, like if A = 4 and B = 5, and working through the logic helps! 

C = max(-A, -B)    # get the maximum of their negatives!
D = C * -1         # since we only need to return the minimum number, C will be it, but as a negative. 
                   # multiply by -1 to convert it back
print(D)


#if you were writing this as a new function, you could do this

def min2(A, B):
    temp = max(-A, -B)
    return temp * -1


