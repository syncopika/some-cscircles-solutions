'''
Define a function postalValidate(S) which first checks if S represents a postal code which is valid:
first, delete all spaces;
the remainder must be of the form L#L#L# where L are letters (in either lower or upper case) and # are numbers.
If S is not a valid postal code, return the boolean False. 
If S is valid, return a version of the same postal code in the nice format L#L#L# where each L is capital.
'''

def postalValidate(S):
   a=S.replace(' ','')  #delete all spaces 
   if a=='':   #if the string is empty, return false
      return False
   elif a[0::2].isalpha() == a[::-2].isdigit() and a[0].isalpha():
      return a.upper()
   return False

'''
more old explanations. from sometime oct 2014.

-edit 083115: for better visualization -
 a - b - c - d - e - f  : example string
 
         ?       ?      <- are these letters?
 
 ? <-this is supposed to be letter
 
     ?       ?       ?  <- are these numbers?
 
let's translate!:
-first step: we need to remove spaces, so just replace ' ' with ''. variable 'a' becomes the revised string with no spaces.
-if a is an empty string, return False (this one surprised me; I only added this part because the cscircles program ran 'S' as ''. otherwise, everything else is correct. I think.)
-otherwise (elif), if it is true that every other character (not including 0) within variable 'a' (i.e. if a = 'abcdef', a[0::2] gives 'ce' -notice how 'a' is excluded) is a letter, 
and it is true that the characters in between (i.e. 'bdf') are numbers, and that the very first character in the string (the 0th char) is a letter, then......(i.e. 'H0H0H0')
-return our string but with all the letters upper-cased.
-if the above wasn't true, return False. 
'''
