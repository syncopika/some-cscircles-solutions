'''
Write a function execute(prog) to do the following. Assume prog is a list of strings containing the BASIC program, like before. 
Then, your function should return either "success" or "infinite loop" depending on whether the program terminates, or loops forever. 
Important: you should assume the procedure findLine(prog, target) defined in sub-task 2 is already defined, you do not need to re-write it.
'''

def execute(prog):
   b=prog[-1].split() #make an array out of the LAST string in prog 
   #the last string contains a number and 'END'. we just need to make sure that this particular number shows up somewhere in the other strings or prog. otherwise, prog will loop infinitely.      
   c=0  #this is our counter
   for i in range(0, len(prog)-1): #now we compare our number against every other string in the array, omitting the last string (the one that we split)
      T=prog[i]
      if b[0] in T:
         c=c+1
   if c==1:         #the number should show up once in another string in order to not loop forever
      return "success"
   return "infinite loop"

