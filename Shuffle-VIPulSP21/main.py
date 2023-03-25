a=input().split()
new=[]
position=1
n=0
if len(a)%2 == 0:
  var1=(len(a)//2)
  var2=(len(a)//2)
  while n<var2:
    new.append(a[n])
    if var1<len(a):
      new.append(a[var1])
      n=n+1
      var1=var1+1
    else:
      n=n+1
      var1=var1+1
  i=0
  while i<len(new)-1:
    a=new[i]
    i=i+1
    print(a,end=" ")
  print(new[-1])
  
else:
  var1=(len(a)//2)+1
  var2=(len(a)//2)+1
  while n<var2:
    new.append(a[n])
    if var1<len(a):
      new.append(a[var1])
      n=n+1
      var1=var1+1
    else:
      n=n+1
      var1=var1+1
  i=0
  while i<len(new)-1:
    a=new[i]
    i=i+1
    print(a,end=" ")
  print(new[-1])
