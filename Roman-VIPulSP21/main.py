i=int(input())
_4=i//1000
print("M"*_4,end="")

i=i%1000
_3=i//100
if _3 < 5:
  print("C"*_3,end="")
elif _3 > 5:
  _3=_3-5
  print("D",end="")
  print("C"*_3,end="")
else:
  print("D",end="")

i=i%100
_2=i//10
if _2 < 5:
  print("X"*_2,end="")
elif _2 > 5:
  _2=_2-5
  print("L",end="")
  print("X"*_2,end="")
else:
  print("L",end="")

i=i%10
if i <= 3:
  print("I"*i)
elif i == 4:
  print("IV")
elif i <= 8:
  print("V",end="")
  i=i-5
  print("I"*i)
elif i==9 :
  print("IX")
else:
  print("X")

# i=int(input())
# 1=="I"
# 5=="V"
# 10=="X"
# 50=="L"
# 100=="C"
# 500=="D"
# 1000=="M"
