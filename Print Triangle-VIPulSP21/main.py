i=int(input())
var=i//2+1
count=0
while count<=i:
  if count%2 != 0:
    print(" "*(i-var)+"*"*count)
    var=var+1
    count=count+1
  else:
    count=count+1
