n=int(input())
lst_str=input()
lst = list(map(int, lst_str.split()))
z=int(input())
a=0
for count in range(n):
  count1=0
  for count1 in range(n):
    if count==count1:
      a=a
    elif lst[count]+lst[count1]==z:
      a=a+1
    else:
      a=a

if a!=0:
  print("YES")
else:
  print("NO")
    
