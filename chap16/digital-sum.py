def digitalSum(n):
  if n == 0: 
      return 0
  return (n % 10 + digitalSum(int(n / 10))) 
    
def digitalSum(n):
   if n < 10:
      return n 
   else:
      return digitalSum(n//10) + digitalSum(n%10)
