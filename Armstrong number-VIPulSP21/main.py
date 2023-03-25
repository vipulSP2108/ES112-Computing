i=input()
number=int(i)
power=len(i)
count=0
sum=0
while count<power:
  num=int(i[count])
  sum=sum+num**power
  count=count+1

if sum==number:
  print("Yes")
else:
  print("No")
