'''
For this program, the first line of input is an integer width. 
Then, there are some lines of text; the line "END" indicates the end of the text. 
For each line of text, you need to print out a centered version of it, by adding periods .. to the left and right, so that the total length of each line of text is width. 
(All input lines will have length at most width.) 
Centering means that the number of periods added to the left and added to the right should be equal if possible; if needed we allow one more period on the left than the right. 
For example, for input:
13
Text
in
the
middle!
END

output:
.....Text....
......in.....
.....the.....
...middle!...

'''

width = int(input())  
while True:
   a=input() 
   b=len(a) #get the length of each word
   c=(width-b)//2  #find the number of extra periods we'll have to add after the word (//2 gives us approx. half the width)
   d=width-(c+b) #this will be the number of periods that need to be added before the word
   e=c*'.'
   f=d*'.'   
   if a=='END':  #end loop once it gets to END
      break
   print(f+a+e)
