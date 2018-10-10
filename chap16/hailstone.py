def hailstone(n):
   n = int(n)
   if n == 1:
      return print(n)
   elif n % 2 == 0:
      print(n)
      hailstone(n/2)
   else:
      print(n)
      hailstone(3*n+1)
