letterGoodness = [0.0817, 0.0149, 0.0278, 0.0425, 0.127, 0.0223, 0.0202, 0.0609, 0.0697, 0.0015, 0.0077, 0.0402, 0.0241, 0.0675, 0.0751, 0.0193, 0.0009, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 0.0007]
#each number corresponds to a letter in the alphabet in sequence, i.e. A, B, C,...

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
