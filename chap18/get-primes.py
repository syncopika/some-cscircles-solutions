def getNonPrimes(n):
   nonprimes = []
   for i in range(2,n+1):
      for j in range(2,i):
         if i%j == 0:
            nonprimes.append(i)
            break
   return nonprimes


def getPrimes(n):
   a = getNonPrimes(n)
   b = []
   c = []
   #fill array with all numbers to n
   for i in range(2,n+1):
      b.append(i)
   #use resulting array from getNonPrimes to eliminate non-primes in b
   for i in range(0,len(b)):
      if b[i] not in a:
         c.append(b[i])
   
   return c
   
   #example: print(getPrimes(10)) => output: [2,3,5,7]
