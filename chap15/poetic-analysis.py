#see http://cscircles.cemc.uwaterloo.ca/15b-python-pushups/

a = input()
words = []
count = []
while a != '###':
   b = a.split()
   for i in range(0,len(b)):
      e = b[i].lower()
      if e not in words:
         words.append(e)
         count.append(1)
      else:
         c = words.index(e)
         count[c] = count[c] + 1
   a = input()

d = count.index(max(count))
print(words[d])
