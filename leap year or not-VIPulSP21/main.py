year=int(input())

if(year<=0):
  print("NO")
elif(year%4==0):
  if (year%100==0 and year%400==0):
       print("YES")
  elif (year%400!=0 and year%100==0):
           print("NO")
  else:     
      print("YES")
  
else:
  print("NO")
