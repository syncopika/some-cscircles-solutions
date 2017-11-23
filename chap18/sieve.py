# coding exercise: primed for takeoff

# this goes from 0 to n. 0 and 1 are predefined as not prime numbers.
# based on the pseudocode shown on wikipedia for sieve of Eratosthenes

def getPrimes(N):
   limit = N
   array = []
   
   # initialize array to all true first
   # this is saying that all numbers will be treated as prime initially
   # we know 0 and 1 are false though 
   array.append(False) # 0
   array.append(False) # 1
   
   # fill rest of table 
   # adding 1 here to N because the upper bound is exclusive, not inclusive.
   for i in range(2, N+1):
      array.append(True)
      
   # now to actually find the composite numbers, which will be marked as false
   # remember that you can limit the upper bound to be the square root of N because any number greater than the 
   # square root of N cannot be a factor of N. this helps reduce the number of iterations needed.
   for j in range(2, int(N**(1/2) + 1)):
      if array[j] == True:
        
		# find all the multiples of j and mark them as false
         k = j*j   # let k be j squared - this is the closest multiple
         l = 0      # this is an additional to be added to k to calculate the next multiple
         nextMultiple = k + l*j    # this is like saying: j^2 + i*j, where i is 0,1,2,...
		 
         # as long as the next multiple is less than the square root of N
         while nextMultiple <= N:
            array[nextMultiple] = False
            l += 1   # increment l, the additional factor
            nextMultiple = k + l*j   # calculate the next multiple
    
   return array
            
#print(getPrimes(100))
isPrime = getPrimes(1000000) # isPrime is a list with true or false, depending if the index is prime or not prime
   
   
#example: print(getPrimes(10))
#output: [False, False, True, True, False, True, False, True, False, False, False]
#         0       1      2      3     4      5     6      7     8      9     10
   
