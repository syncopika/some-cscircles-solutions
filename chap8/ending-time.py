'''
This program takes two lines of input. The first line is a "starting time" expressed in a 24-hour clock with leading zeroes, like 08:30 or 14:07. 
The second line is a duration D in minutes. 
Print out what time it will be D minutes after the starting time. For example, for input:
12:30
47
the correct output would be 13:17. 
All times should be formatted as numbers between 00:00 and 23:59, but the time period may go over midnight. 
For example, on input
23:59
13
the correct output is 00:12.
'''

time=input()  #first string
D=int(input()) #second string
st1=int(time[0:2]) #get the hours  (first half of string)
st2=int(time[3:5]) #get the minutes (second half of string)
nt=(D+st2)%60          #add the additional minutes (provided by the second string) to the current minutes
st1=st1+(D+st2)//60%24   #given the new number of minutes, we'll calculate what the new hours should be
if st1==24:     #set some conditions. if st1 is 24, make it 00. 
   st1='00'
if nt<10:          #add a leading zero if the hours is less than 10
   nt='0'+str(nt)
if int(st1)>24:       
   st1='0'+str(st1%24)
print(str(st1)+':'+str(nt))
