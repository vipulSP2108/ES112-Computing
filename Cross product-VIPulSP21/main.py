def CrossProduct(x, y):
  #the cross product of x and y
  x=list(x)
  y=list(y)
  # for len(x)< 3:
  #   x.append(0)
  # for len(y)< 3:
  #   y.append(0)
  while len(x)< 3:
    x.append(0)
  while len(y)< 3:
    y.append(0)
  
  cross_product=[((x[1]*y[2])-(x[2]*y[1])),((x[2]*y[0])-(x[0]*y[2])),((x[0]*y[1]-x[1]*y[0]))]
  cross_product=tuple(cross_product)
  return cross_product
  pass
  
### Do NOT edit the code below!
x = tuple(map(int, input().split()))
y = tuple(map(int, input().split()))
z = CrossProduct(x, y)
assert isinstance(z, tuple)
print(z)
