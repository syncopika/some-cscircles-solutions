def countup(n):
  if n == 1:
    print('Blastoff!')
  else:
    countup(n - 1)
  print(n)
