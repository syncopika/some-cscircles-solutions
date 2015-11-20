#finally, after seeing this problem many months ago, I got around to solving it! 7:30 pm est 11/19/15

a = 32 #begin with the character that is number 32
for i in range(0, 12):
   row = "";
   if i%2 == 0:
      row += "chr: "; #odd row = chr
   else:
      row += "asc: "; #even row = asc
   for j in range(a, a+16):
      if i%2 == 0:
         row += " " + chr(j) + "  ";
      else:
         if j < 100:
            row += str(j) + "  ";
            a = a+1;  #only increment variable 'a' when the loop reaches a row that prints the numbers
         else:        #when this inner loop ends, the new value of 'a' should be 16 more than it was before.
            row += str(j) + " ";
            a = a+1;
   print(row);
