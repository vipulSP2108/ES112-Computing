i=input().split()
listx=list(map(int,i))
for count in range(2):
  max1=max(listx)
  listx.remove(max1)
print(max1)

# a = list(map(int,input().split()))
# a.sort()
# print(a[len(a)-2])
