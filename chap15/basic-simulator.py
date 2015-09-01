# def getBASIC from subtask 1
def getBASIC():
   b=[]
   while True:
      a=input()
      b.append(a)
      if a.endswith("END") == True:
         break
   return b
     
# def findLine from subtask 2
def findLine(prog, target):
   for i in prog:
      x=i.split()
      if x[0] == target:
         return prog.index(i)

# def execute from subtask 3
def execute(prog):
   c=prog[-1].split()
   d=0
   for location in range(0, len(prog)-1):
      T=prog[location]
      if c[0] in T:
         d=d+1
   if d==1:
      return "success"
   return "infinite loop"
   


print(execute(getBASIC()))
