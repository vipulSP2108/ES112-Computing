# 3 + 1²/(6 + 3²/(6 + 5²/(6 + 7²/...)))

i=int(input())
if i==0 :
  print("3")
elif i==1 :
  print("19/6")
else:
  new=[]
  a=0
  while a<= i*2:
    if a%2!=0 and a!=1 :
      new.append(a)
      a=a+1
    else:
      a=a+1
  new.reverse()
    
  b=1
  c=0
  d=1
  count=1
  q=0
  while c<len(new):
    if b==1:
      q=6
    w=new[c]
    number=6*q+(w**2)*d
    d=q
    q=number
    b=b+1
    c=c+1

  final_1=(3*number)+d
  final_2=number

  from fractions import Fraction
  print(Fraction(final_1,final_2))      

# i=int(input())
# count=0
# q=3
# z=1
# while count<i:
#   w=(2*z-1)
#   q=q+((w**2),"/",6)
#   z=z+1
#   count=count+1
# print(q)
    
