'''
for this task, we want to ensure that the program follows the instructions of a BASIC program. in this subtask, a sample input would be "findLine(['10 GOTO 20','20 END'], '10')". 
the output should be '0' because the second parameter, 10, is found in the 0th index of the list (the first parameter).
'''

def findLine(prog, target):
   for i in prog:
      x=i.split()    #here we're making a new array from a string so we can access the 0th element of the string
      if x[0] == target:  #for each string in the array, check the 0th element. if it equals our target, tell us the index of the string it was found in 
         return prog.index(i)

'''
old explanation: (i do like the visual though!)

translation:
-so first we set up the function with two parameters, prog and target. target is what we want to find in prog.
-notice in the example input how each index in the list is a phrase with spaces, i.e. '10 GOTO 20' and '20 END'.
-in order to locate where in 'prog' the 'target' shows up, we need to make a list out of each element in 'prog' to separate out each word or number.
-then we'll get '10 GOTO 20' => ['10','GOTO','20'] and now we can try matching each of those elements to our 'target'.
-to do this, a for loop works. for each element (i) in prog:...
-assign a variable to hold each split element from prog (i.e. 1 split element would be ['10','GOTO','20']. another would be ['20,'END']. i used 'x' as my variable.
-now we have to set a condition. if the first element in our new list, 'x', matches our target, then...
-this gets a bit confusing (at least for me), so I'll try visualizing it:
                      prog => ['10 GOTO 20', '20 END']    this is one list
                      index:       0             1
                                  /                 \
                                 /                   \
                      x=> ['10','GOTO','20'], ['20','END']   this is now two lists
                   index:   0     1      2       0    1
                      answer =>  ah! our target, '10', is the 0th element in that first list of x, which is in the 0th element of prog! 
- now using our code, 'return prog.index(i)', we're saying, "after you find our target, tell me where the target is relative to the index in prog. in this case, 10 is in the 0th element of prog."
- notice how we picked the 0th element for x. This is because we want to ensure that the program can move line to line, and so it's the first number that matters.
'''
  
