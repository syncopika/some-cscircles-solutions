#this one stumped me for a while...the thing I was missing was setting variable a to equal the recursive function!
#by making a = nestedListContains(NL[x], target), a will keep getting updated until the recursion is finished, resulting
#in either a being True or False. 

def nestedListContains(NL, target):
   a = False
   for x in range(0,len(NL)):
      print(NL[x])
      
      if NL[x] == target:
         a = True
      
      if type(NL[x]) != int:
            a = nestedListContains(NL[x], target)
   return a  
