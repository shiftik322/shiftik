for i in range (550001, 550100):
   for x in range(2, i//2):
      if i%x == 0:
         t =  i/x
         for y in range(2, i//x):
           if t%y == 0:
              print(i)
              break
         break   
