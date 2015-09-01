'''
Using index and other list methods, write a function replace(list, X, Y) which replaces all occurrences of X in list with Y. 
For example, if L = [3, 1, 4, 1, 5, 9] then replace(L, 1, 7) would change the contents of L to [3, 7, 4, 7, 5, 9].
To make this exercise a challenge, you are not allowed to use []. 
Note: you don't need to use return. 
'''

def replace(list, X, Y):
   while X in list:  #as long as there's still an instance of X in the list...
      a=list.index(X)  #get X's index
      list.remove(X)   #take it out
      list.insert(a,Y)  #replace with Y
      
      
'''
here's an old attempt at explaining this I did many months ago...(on 9 Oct 2014 )

let's translate this!
-the function replace() needs three parameters to work: the list, any value for X and Y (so long as they're in the list)
-ok, now we translate:
- while X still continues to exist in the list,
- we'll define variable 'a' as the location where X is located (thus, list.index(X))
- then, let's remove the X's since we want to replace them with Y.
- even though the X's are gone, we've logged where each one is (with variable 'a', remember?)
- so now, all we have to do is note the locations and insert Y where the X's were (thus, list.insert(a, Y)).
'''
