i1=int(input())
count=1
a=[]
while count <= i1:
  a=a+[input().split()]
  count=count+1

i=int(input())
count=1
while count<=i:
  city=input()
  v=0
  while v<i1:
    if city in a[v]:
      print(a[v][0])
      break
    else:
      v=v+1
  count=count+1
  
# 2
# USA Boston Pittsburgh Washington Seattle
# UK London Edinburgh Cardiff Belfast
# 3
# Cardiff
# Seattle
# London








# if ai in a:
#   print(a1)
# else:
#   print("NO")
