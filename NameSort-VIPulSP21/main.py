i= int(input())
firstname_s=[]
secondname_s=[]
sorted=[]
count=0
while count < i:
  firstname,secondname=input().split()
  firstname_s=firstname_s+[firstname]
  secondname_s=secondname_s+[secondname]
  sorted=sorted+[secondname]
  count=count+1 

secondname_s.sort()
var1=0
while var1 < i:
  var2=0
  while var2< i:
    if secondname_s[var1]==sorted[var2]:
      print(firstname_s[var2],sorted[var2])
    var2=var2+1
  var1=var1+1
