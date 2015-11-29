#a 'regular' sieve of Eratosthenes
#this goes from 0 to n. 0 and 1 are predefined as not prime numbers.

def getPrimes(n):
   isPrime = [False, False]
   for i in range(2,n+1): #n+1 so that whatever n is is included in the answer
      isPrime.append(True)
      
   for i in range(2,n+1):    #go through each index in isPrime (excluding the first two indices)
      if isPrime[i] == True: #is this statement really necessary?
         for j in range(0,n+1):
            if((i**2 + i*j) < n+1):
               isPrime[i**2 + i*j] = False
            
   return isPrime
   
   
#example: print(getPrimes(10))
#output: [False, False, True, True, False, True, False, True, False, False, False]
#         0       1      2      3     4      5     6      7     8      9     10
   
