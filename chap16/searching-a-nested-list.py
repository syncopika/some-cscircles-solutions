#this one stumped me for a while...the thing I was missing was setting variable a to equal the recursive function!

#By making a = nestedListContains(NL[x], target), a will keep getting updated until the recursion is finished, resulting
#in either a being True or False. 

#I put in a break because check out this test without the break statement: 
#print(nestedListContains([3,7,[5],9], 7))

#The above should return True, but it doesn't without the break. (interestingly, omitting the break still satisfies
#cscircles tests.) 

#I think this is because even though at some point the loop will return True, there is still one
#more nested list to go through (the [5]), so that finally when the recursion ends, variable a will equal False (because
#of the 5) and so the final result if False, which is incorrect. The break will make the loop stop wherever a = True. 

def nestedListContains(NL, target):
   a = False
   for x in range(0,len(NL)):
      print(NL[x])#not needed, but helps to make sure loop is working as intended
      
      if NL[x] == target:
         a = True
         break #I think this is necessary to ensure that True is returned
      
      if type(NL[x]) != int:
            a = nestedListContains(NL[x], target)
   return a  
