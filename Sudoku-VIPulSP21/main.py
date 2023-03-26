n=int(input())
n_2=n**2
final=0

count=1
orignal=[]
while count<=n_2:
  orignal.append(count)
  count=count+1
org=list(map(int,orignal))

listx=[]
for aa in range(n_2):
  aa=list(map(int,input().split()))
  listx.append(aa) 
## row
var1=0
count=0
col_ele=0
while var1<n_2 :
  var2=0
  list1=[]
  while var2<n_2:
    list1.append(listx[var1][var2])
    var2=var2+1
  list1.sort()
  if list1==org:
    col_ele=col_ele
  else:
    col_ele=col_ele+1
  var1=var1+1
if col_ele==0:
 final=final
else:
 final=final+1
##vertical
var1=0
count=0
col_ele=0
while var1<n_2:
  var2=0
  list1=[]
  while var2<n_2:
    list1.append(listx[var2][var1])
    var2=var2+1
  list1.sort()
  if list1==org:
    col_ele=col_ele
  else:
    col_ele=col_ele+1  
  var1=var1+1
if col_ele==0:
  final=final
else:
  final=final+1
##squar  
for col in range(0,n_2,n):
  x=col
  y=col 
  x=x+n
  for row in range(0,n_2,n):
    z=row
    z=z+n
    list9=[]
    while row<z:
      col=y
      while col<x:
        list9.append(listx[row][col])
        col=col+1
      row=row+1
    list9.sort()
    if list9==org:
      final=final
    else:
      final=final+1
if final==0:
  print("Yes")
else:
  print("No")

# for i in range(0,n_2,n):
#   x=i
#   y=n+i
#   set={()}
#   for i in range(x,y):
#     for x in range(x,y):
  #     set.add(list[i][x])
  # if list1==org:
  #   final=final
  # else:
  #   final=final+1




  
# n=int(input())
# n_2=n**2
# final=0

# count=1
# orignal=[]
# while count<=n_2:
#   orignal.append(count)
#   count=count+1
# org=list(map(str,orignal))

# count=0
# row_ele=0
# list=[]
# while count<n_2:
#   aa=input().split()
#   list.append(aa)
#   count=count+1
# for col in range(0,n_2,n):
#   x=col
#   y=col 
#   x=x+n
#   for row in range(0,n_2,n):
#     z=row
#     z=z+n
#     list1=[]
#     while row<z:
#       col=y
#       while col<x:
#         list1.append(list[row][col])
#         col=col+1
#       row=row+1
#     list1.sort()
#     if list1==org:
#       final=final
#     else:
#       final=final+1

# if final==0:
#   print("Yes")
# else:
#   print("No")
