i=int(input())
a=0
b=1
c=1
count=1

while count<=i:
  if c%2==0:
    print(c)
    c=a+b
    a=b
    b=c
    count=count+1
  else:
    c=a+b
    a=b
    b=c
