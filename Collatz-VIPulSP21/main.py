n=int(input())
if n != 1:
  print(n,end=" ")
  while True:
    if n == 1:
      print(1)
      break
    if n%2!=0 :
      n=(3*n)+1
      print(n,end=" ")
    else :
      if n != 2:
        n=n//2
        print(n,end=" ")
      else:
        n=n//2
        continue
else:
  print(n)

