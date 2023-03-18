def num(i):
  a=0
  for factor in range(1,i):
    if i%factor==0:
      a=a+factor
    else:
      a=a
  return a
  
n=int(input())
count=0
while count<n:
  b=int(input())
  if num(b)==b:
    print("YES")
  else:
    print("NO")
  count=count+1