a=int(input())

rem=0
i=0
no=0

while a>0 :
  rem=a%2
  no=no+rem*(10**i)
  a=a//2
  i=i+1

print(no)
