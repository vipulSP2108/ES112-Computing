q=0
w=0
e=0
totel=0
import random
while True :
  user=input()
  # import random
  com=random.choice(["r","p","s"])
  
  if user=="end":
    break  
  elif(com=="r" and user=="s" or
  com=="s" and user=="p" or
  com=="p" and user=="r"):
    q=q+1
    totel=totel+1
    print("TOTEL",totel)
    print(com,"beats",user,";","computer wins") 
    print("computer",q,"user",w,"draw",e)
  elif(com=="s" and user=="r" or
  com=="r" and user=="s" or
  com=="r" and user=="p"):
    w=w+1
    totel=totel+1
    print("TOTEL",totel)
    print(user,"beats",com,";","user wins") 
    print("computer",q,"user",w,"draw",e)
  else:
    e=e+1
    totel=totel+1
    print("TOTEL",totel)
    print("draw")
    print("computer",q,"user",w,"draw",e)
  print('print end for results')
print("*"*40)
print("TOTEL",totel)
print("computer",q,"user",w,"draw",e)
print()
qq=q-w
ww=w-q
if q>w:
  print("WINNER is \n COMPUTER by",qq,"points")
else:
  print("WINNER is \n USER by",ww,"points")


# q=0
# w=0
# r="rock"
# p="paper"
# s="scisser"
# while True :
#   user=input()
#   import random
#   com=random.choice([r,p,s])
#   if(com==r and user==s or
#   com==s and user==p or
#   com==p and user==r):
#     q=q+1
#     print(com,"beats",user,";","computer wins") 
#     print("computer",q,"user",w)
#   elif(com=="s" and user=="r" or
#   com==r and user==s or
#   com==r and user==p):
#     w=w+1
#     print(user,"beats",com,";","user wins") 
#     print("computer",q,"user",w)
#   else:
#     print("draw")
#     print("computer",q,"user",w)
  
