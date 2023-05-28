x1,x2,x3,x4,x5=input().split(" ")
o1,o2,o3,o4=input().split(" ")

x={x1,x2,x3,x4,x5}
o={o1,o2,o3,o4}

win= [{"4","6","2"} , {"4","0","8"} , {"1","0","2"},{"4","5","3"} , {"7","8","6"} , {"0","3","6"} ,{"4","7","1"} , {"8","5","2"}]

i=0
while i<= 7:
  if win[i].issubset(x)==True:
    print("x")
    break
  if win[i].issubset(o)==True:
    print("o")
    break
    # i=i+1
  elif i==7 :
    print("draw")
  i=i+1

  
# if win[0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 ].issubset(x)==True:
#   print("x")
  
# if win[0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 ].issubset(o)==True:
#   print("o")

# else:
#   print("draw")


# x=input().split(" ")
# o=input().split(" ")

# if(("4" in x or "6"in x or "2"in x) and
#   ("4" in x or "0"in x or "8"in x) and
#   ("1"in x or "0"in x or "2"in x) and
#   ("4"in x or "5"in x or "3"in x) and
#   ("7"in x or "8"in x or "6"in x) and
#   ("0"in x or "3"in x or "6"in x) and
#   ("4"in x or "7"in x or "1"in x) and
#   ("8"in x or "5"in x or "2"in x) ):
#   print("x")

# elif(("4" in o or "6"in o or "2"in o) and
#   ("4" in o or "0"in o or "8"in o) and
#   ("1"in o or "0"in o or "2"in o) and
#   ("4"in o or "5"in o or "3"in o) and
#   ("7"in o or "8"in o or "6"in o) and
#   ("0"in o or "3"in o or "6"in o) and
#   ("4"in o or "7"in o or "1"in o) and
#   ("8"in o or "5"in o or "2"in o) ):
#   print("o")
    
# # elif({"4","6","2"}in o or 
# #    {"4","0","8"} in o or 
# #    {"1","0","2"} in o or 
# #    {"4","5","3"} in o or 
# #    {"7","8","6"} in o or 
# #    {"0","3","6"} in o or
# #    {"4","7","1"} in o or 
# #    {"8","5","2"} in o):
# #   print("o")

# else:
#   print("draw")
