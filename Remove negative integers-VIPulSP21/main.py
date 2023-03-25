lst_str=input()
lst = list(map(int, lst_str.split()))
a=[]
for i in lst:
  if i>=0 :
    a.append(i)

q=0
# for i in range(len(a)):
#   print(a[i],end=" ")
while q<len(a):
  print(a[q],end=(" "))
  q=q+1
    
