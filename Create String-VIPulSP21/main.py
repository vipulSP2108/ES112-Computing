import string

stra=""
for letter in string.ascii_lowercase:
  stra=stra+letter

strA=""
for letter in string.ascii_uppercase:
  strA=strA+letter

s=input()
listx=[]
for count in range(len(s)):
  listx.append(s[count])

NP=input()
count=0
while count<len(s):
  a=stra.find(s[count])
  A=strA.find(s[count])
  
  if NP[count]=="N" and A==-1:
    print(stra[a+1],end="")
  elif NP[count]=="P" and A==-1:
    print(stra[a-1],end="")
    
  if NP[count]=="N" and a==-1:
    print(strA[A+1],end="")
  elif NP[count]=="P" and a==-1:
    print(strA[A-1],end="")

  count=count+1
