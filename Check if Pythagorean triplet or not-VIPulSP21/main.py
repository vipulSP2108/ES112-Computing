no_1=int(input())
no_2=int(input())
no_3=int(input())
if(no_1<0 or no_2<0 or no_3 <0):
  print("NO")
elif(no_1**2+no_2**2==no_3**2):
  print("YES")
elif(no_2**2+no_3**2==no_1**2):
  print("YES")
elif(no_3**2+no_1**2==no_2**2):
  print("YES")
else:
  print("NO")
