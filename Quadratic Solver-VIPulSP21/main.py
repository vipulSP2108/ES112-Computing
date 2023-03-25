a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)

D=(b**2)-(4*a*c)
D2=D**1/2 
D2=int(D2)

if D>=0 and (D**1/2)%1==0 :
  x1=(-b+D2)/(2*a)
  x2=(-b-D2)/(2*a)
  x1=int(x1)
  x2=int(x2)
  x1=str(x1)
  x2=str(x2)
  print("("+x1+",",x2+")")

if D>=0 and (D**1/2)%1!=0 :
  D=str(D)
  b=str(b)
  print("(-"+b,"± √"+D+")/2" )

if D<0:
  D=-D
  if D**1/2%1==0:
    D=D**(1/2)
    D=int(D)
    D=str(D)
    b=str(b)
    print("(-"+b,"± i"+D+")/2")
  else :
    b=str(b)
    D=str(D)
    print("(-"+b,"± i√"+D+")/2")
