def digitalRoot(n):
  if n > 9:
     return digitalRoot(digitalSum(n))
  else:
     return n
