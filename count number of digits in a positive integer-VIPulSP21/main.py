i=int(input())
a=0
q=0
w=0
while i!= 0:
  a=i%10
  if(a<10):
    w=w+1
  else:
    w=w
  i=i//10
print(w)
