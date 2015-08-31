#Write a program that takes a single input line of the form «number1»+«number2», where both of these represent positive integers, and outputs the sum of the two numbers. 
#For example on input 5+12 the output should be 17.

S = input()
for position in range(0, len(S)):
   if S[position] == '+':       #find where the numbers are split by the plus sign
      str1 = int(S[0:position]) #turns str1 into number1
      str2 = int(S[position:len(S)])  #turns str2 into number2
      print(str1 + str2)
