i=input()
length=len(i)
i=int(i)
last_digit=0
dec=0
count=0
var1=0
while count<length:
  last_digit=i%10
  var1=dec
  dec=last_digit*(2**count)
  dec=var1+dec
  i=i//10
  count=count+1
print(dec)
