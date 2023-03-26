s=input()

listx=[]
for count in range(len(s)):
  listx.append(s[count])
  
count=1
n=0
while count<len(listx):
  k=listx[n]
  listx.remove(listx[n])
  listx.insert(count,k)
  count=count+2
  n=n+2
print("".join(listx))
