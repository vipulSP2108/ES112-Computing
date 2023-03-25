lst_str=input()
lst = list(map(int, lst_str.split()))

i=0
even=0
odd=0

while i<=len(lst)-1:
  if lst[i]%2==0:
    even=even+1
  else:
    odd=odd + 1
  i=i+1
  
print(even,odd)
