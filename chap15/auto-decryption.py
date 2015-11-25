def decrypt(thing):
   a = thing
   alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
   shifts = [] #collect all shift variations
   shiftGoodness = [] #collects all variations' goodness
   
   for i in range(1, 27): #check shift of 1 to 26. 
      newShift = []
      for letter in range(0,len(a)):
         if a[letter] != ' ':
            newOrder = ord(a[letter]) - i
            if newOrder < 65:
               newOrder = newOrder + 26
            newShift.append(chr(newOrder))
         else:
            newShift.append(a[letter]) #this will catch any spaces
      shifts.append(newShift)
      goodness = [] #use this list to calculate goodness of each newShift
      
      for i in range(0,len(newShift)):
         if newShift[i] != ' ': #ignore spaces
            b = alphabet.index(newShift[i])
            goodness.append(letterGoodness[b])
      shiftGoodness.append(sum(goodness))
   
   c = shiftGoodness.index(max(shiftGoodness))
   decrypted = ''
   
   for i in range(0,len(shifts[c])):
      decrypted += shifts[c][i]
   print(decrypted)
#end of decrypt

thing = input()
decrypt(thing)
