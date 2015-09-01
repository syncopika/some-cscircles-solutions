'''
Write a function getBASIC() which takes no arguments, and does the following: it should keep reading lines from input using a while loop; 
when it reaches the end it should return the whole program in the form of a list of strings. 
'''

def getBASIC():
   b=[]
   while True:
      a=input()
      b.append(a)    
      if a.endswith("END") == True:
         break
   return b
   
'''
083115
in retrospect, i'm not quite sure why i thought i needed such a long-winded explanation for a relatively straight-forward problem.
however, i believe i do recall how difficult it was to grasp these concepts and to apply them when i saw them for the first time.
it's easy to forget these basic things too after spending a period of time away from practicing programming. but if you do them enough times,
these algorithm problems, it should start to stick pretty well, hopefully forever!

old explanation:

translation:
-first define your function -> getBasic() 
-next, you want your function to keep collecting inputs until one of the inputs ends with "END". the best way I know how to do that is to use a list ([]) to continuously collect. It looks like I'll also need a loop to do that.
-so first we assign our list a variable. I used 'a' here. a=[]
-next, we want to have this loop keep on going, and there are no number ranges here, no counters, no < or >. so just use "while True".
-now we can assign a variable to input(), the stuff we're going to keep collecting in 'a', our currently empty list. i used 'b' for input().
-then we make sure we keep adding b to a, so I use the "append" method. just put "b.append(a)". 
-now we put a condition so we can stop the loop. this one is a straightforward if-statement, simply saying "if one of the inputs ends with "END", stop the loop!"
-finally we 'return b'. 'b' now holds all the inputs up until the one ending with 'END'.
'''
