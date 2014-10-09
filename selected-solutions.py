#disclaimer: some of my explanations will probably suck. sorry. I'll try to always come back and proofread to improve explanations. constructive criticism will be appreciated too! :D  
#this is mainly to help myself practice explaining things I guess, and logging my Python practice experience.
#just to keep track of progress: I started these explanations maybe ~2 months ago, attempted serious Python study maybe ~3 months ago?
#please note this is Python 3


#14-methods

#coding exercise: the replacements

'''

the instructions:
Using index and other list methods, write a function replace(list, X, Y) which replaces all occurrences of X in list with Y.   
For example, if L = [3, 1, 4, 1, 5, 9] then replace(L, 1, 7) would change L to [3, 7, 4, 7, 5, 9]. 
To make this exercise a challenge, you are not allowed to use []. 
Note: you don't need to use return. 

'''

def replace(list, X, Y):
   while X in list:
      a=list.index(X)
      list.remove(X)
      list.insert(a, Y)

'''
let's translate this!
-the function replace() needs three parameters to work: the list, any value for X and Y (so long as they're in the list)
-ok, now we translate:
- while X still continues to exist in the list,
- we'll define variable 'a' as the location where X is located (thus, list.index(X))
- then, let's remove the X's since we want to replace them with Y.
- even though the X's are gone, we've logged where each one is (with variable 'a', remember?)
- so now, all we have to do is note the locations and insert Y where the X's were (thus, list.insert(a, Y)).
'''


#coding exercise: exact postage
'''
the instructions:
Define a function postalValidate(S) which first checks if S represents a postal code which is valid:
first, delete all spaces;
the remainder must be of the form L#L#L# where L are letters (in either lower or upper case) and # are numbers.
If S is not a valid postal code, return the boolean False. If S is valid, return a version of the same postal code in the nice format L#L#L# where each L is capital.

'''

def postalValidate(S):
   a=S.replace(' ','')
   if a == '':
      return False
   elif a[0::2].isalpha() == a[::-2].isdigit() and a[0].isalpha():
      return a.upper()
   return False

'''
let's translate!:
-first step: we need to remove spaces, so just replace ' ' with ''. variable 'a' becomes the revised string with no spaces.
-if a is an empty string, return False (this one surprised me; I only added this part because the cscircles program ran 'S' as ''. otherwise, everything else is correct. I think.)
-otherwise (elif), if it is true that every other character (not including 0) within variable 'a' (i.e. if a = 'abcdef', a[0::2] gives 'ce' -notice how 'a' is excluded) is a number, 
it is true that the characters in between (i.e. 'bdf') are numbers, and that the very first character in the string (the 0th char) is a letter, then......(i.e. 'H0H0H0')
-return our string but with all the letters upper-cased.
-if the above wasn't true, return False. 
'''

15A #a Python program that reads a BASIC program as input

#Sub-task 1: reading the program 

def getBASIC():
   b=[]
   while True:
   a=input()
   b.append(a)
   if a.endswith("END") == True:
      break
   return a

'''
translation:
-first define your function -> getBasic() 
-next, you want your function to keep collecting inputs until one of the inputs ends with "END". the best way I know how to do that is to use a list ([]) to continuously collect. It looks like I'll also need a loop to do that.
-so first we assign our list a variable. I used 'a' here. a=[]
-next, we want to have this loop keep on going, and there are no number ranges here, no counters, no < or >. so just use "while True".
-now we can assign a variable to input(), the stuff we're going to keep collecting in 'a', our currently empty list. i used 'b' for input().
-then we make sure we keep adding b to a, so I use the "append" method. just put "b.append(a)". 
-now we put a condition so we can stop the loop. this one is a straightforward if-statement, simply saying "if one of the inputs ends with "END", stop the loop!"
-finally we 'return a'. 'a' now holds all the inputs up until the one ending with 'END'.

'''

#Sub-task 2: go to it!

#for this task, we want to ensure that the program follows the instructions of a BASIC program. in this subtask, a sample input would be "findLine(['10 GOTO 20','20 END'], '10')". 
#the output should be '0' because the second parameter, 10, is found in the 0th index of the list (the first parameter).

def findLine(prog, target):
   for i in prog:
      x=i.split()
      if x[0] == target:
         return prog.index(i)

'''
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
  
