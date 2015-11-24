def choose(n, k):
   product = 1
   diff = n - k 
   while k > 0:
      product = (diff+k)/k*product
      k = k - 1
   return product
